def predict_loan_eligibility(user_data, bank_id, loan_id):
    """
    Enhanced prediction that considers both user profile and specific loan criteria

    Args:
        user_data: User's financial information
        bank_id: Selected bank ID
        loan_id: Selected loan product ID

    Returns:
        dict: Detailed eligibility assessment
    """
    from ..data.bank_loans import get_loan_details, BANK_LOAN_PRODUCTS

    # Get loan criteria
    loan_details = get_loan_details(bank_id, loan_id)
    if not loan_details:
        return {"error": "Invalid bank or loan selection"}

    criteria = loan_details["eligibility_criteria"]

    # Initialize scoring
    eligibility_score = 0.0
    max_score = 100.0
    reasons = []

    # 1. CIBIL Score Check (25 points)
    user_cibil = float(user_data.get('cibil_score', 300))
    min_cibil = criteria.get('min_cibil_score', 650)

    if user_cibil >= min_cibil:
        if user_cibil >= 800:
            eligibility_score += 25
            reasons.append("Excellent credit score")
        elif user_cibil >= 750:
            eligibility_score += 20
            reasons.append("Very good credit score")
        elif user_cibil >= 700:
            eligibility_score += 15
            reasons.append("Good credit score")
        else:
            eligibility_score += 10
            reasons.append("Acceptable credit score")
    else:
        eligibility_score -= 20
        reasons.append(f"Credit score below minimum requirement ({min_cibil})")

    # 2. Income Check (20 points)
    user_income = float(user_data.get('income_annum', 0))
    min_income = criteria.get('min_income_annum', 200000)

    if user_income >= min_income:
        if user_income >= min_income * 2:
            eligibility_score += 20
            reasons.append("Excellent income level")
        elif user_income >= min_income * 1.5:
            eligibility_score += 15
            reasons.append("Good income level")
        else:
            eligibility_score += 10
            reasons.append("Meets minimum income requirement")
    else:
        eligibility_score -= 15
        reasons.append(f"Income below minimum requirement (₹{min_income:,})")

    # 3. Loan-to-Income Ratio Check (15 points)
    loan_amount = float(user_data.get('loan_amount', 0))
    max_lti_ratio = criteria.get('max_loan_to_income_ratio', 3.0)
    actual_lti_ratio = loan_amount / user_income if user_income > 0 else float('inf')

    if actual_lti_ratio <= max_lti_ratio:
        if actual_lti_ratio <= max_lti_ratio * 0.7:
            eligibility_score += 15
            reasons.append("Conservative loan-to-income ratio")
        else:
            eligibility_score += 10
            reasons.append("Acceptable loan-to-income ratio")
    else:
        eligibility_score -= 15
        reasons.append(f"Loan-to-income ratio too high (max: {max_lti_ratio:.1f})")

    # 4. Bank Assets Check (10 points)
    user_bank_assets = float(user_data.get('bank_asset_value', 0))
    min_bank_assets = criteria.get('min_bank_assets', 25000)

    if user_bank_assets >= min_bank_assets:
        if user_bank_assets >= min_bank_assets * 3:
            eligibility_score += 10
            reasons.append("Strong savings buffer")
        else:
            eligibility_score += 5
            reasons.append("Adequate savings")
    else:
        eligibility_score -= 10
        reasons.append(f"Insufficient bank balance (min: ₹{min_bank_assets:,})")

    # 5. Employment Type Check (10 points)
    user_employment = user_data.get('self_employed', 'No').lower()
    allowed_employment = criteria.get('employment_types', ['salaried', 'self_employed'])

    employment_mapping = {
        'no': 'salaried',
        'yes': 'self_employed'
    }

    user_emp_type = employment_mapping.get(user_employment, user_employment)

    if user_emp_type in allowed_employment:
        eligibility_score += 10
        reasons.append(f"Eligible employment type: {user_emp_type}")
    else:
        eligibility_score -= 10
        reasons.append(f"Employment type not eligible for this loan")

    # 6. Loan Amount Range Check (10 points)
    min_amount = loan_details["amount_range"]["min"]
    max_amount = loan_details["amount_range"]["max"]

    if min_amount <= loan_amount <= max_amount:
        eligibility_score += 10
        reasons.append("Loan amount within acceptable range")
    else:
        eligibility_score -= 10
        reasons.append(f"Loan amount outside range (₹{min_amount:,} - ₹{max_amount:,})")

    # 7. Loan Term Check (10 points)
    loan_term = float(user_data.get('loan_term', 360))
    min_term = loan_details["term_range"]["min_months"]
    max_term = loan_details["term_range"]["max_months"]

    if min_term <= loan_term <= max_term:
        eligibility_score += 10
        reasons.append("Loan term within acceptable range")
    else:
        eligibility_score -= 10
        reasons.append(f"Loan term outside range ({min_term}-{max_term} months)")

    # Calculate final eligibility
    eligibility_percentage = max(0, min(100, eligibility_score))

    if eligibility_percentage >= 80:
        status = "Approved"
        confidence = "High"
    elif eligibility_percentage >= 60:
        status = "Approved"
        confidence = "Medium"
    elif eligibility_percentage >= 40:
        status = "Under Review"
        confidence = "Low"
    else:
        status = "Rejected"
        confidence = "High"

    return {
        "bank_name": loan_details["bank_name"],
        "loan_name": loan_details["loan_name"],
        "eligibility_status": status,
        "eligibility_score": round(eligibility_percentage, 1),
        "confidence": confidence,
        "reasons": reasons,
        "loan_details": {
            "amount_range": loan_details["amount_range"],
            "term_range": loan_details["term_range"],
            "interest_rate": loan_details["interest_rate_range"],
            "processing_fee": loan_details["processing_fee"]
        }
    }