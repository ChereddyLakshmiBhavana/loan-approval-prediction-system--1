# Bank and Loan Products Database
# This would typically be in a database, but using Python dict for demo

BANK_LOAN_PRODUCTS = {
    "SBI": {
        "name": "State Bank of India",
        "loans": {
            "home_loan": {
                "name": "Home Loan",
                "min_amount": 300000,
                "max_amount": 50000000,
                "min_term_months": 60,
                "max_term_months": 360,
                "interest_rate_range": "6.65% - 7.15%",
                "eligibility_criteria": {
                    "min_cibil_score": 650,
                    "min_income_annum": 300000,
                    "max_loan_to_income_ratio": 5.0,
                    "min_bank_assets": 50000,
                    "employment_types": ["salaried", "self_employed"],
                    "age_range": [21, 70]
                },
                "processing_fee": "0.5% of loan amount",
                "prepayment_charges": "2% + applicable taxes"
            },
            "personal_loan": {
                "name": "Personal Loan",
                "min_amount": 50000,
                "max_amount": 2000000,
                "min_term_months": 12,
                "max_term_months": 84,
                "interest_rate_range": "10.45% - 16.45%",
                "eligibility_criteria": {
                    "min_cibil_score": 650,
                    "min_income_annum": 200000,
                    "max_loan_to_income_ratio": 2.0,
                    "min_bank_assets": 25000,
                    "employment_types": ["salaried"],
                    "age_range": [21, 58]
                },
                "processing_fee": "1% of loan amount",
                "prepayment_charges": "Nil"
            }
        }
    },
    "HDFC": {
        "name": "HDFC Bank",
        "loans": {
            "home_loan": {
                "name": "Home Loan",
                "min_amount": 100000,
                "max_amount": 10000000,
                "min_term_months": 60,
                "max_term_months": 360,
                "interest_rate_range": "6.60% - 7.10%",
                "eligibility_criteria": {
                    "min_cibil_score": 650,
                    "min_income_annum": 250000,
                    "max_loan_to_income_ratio": 4.5,
                    "min_bank_assets": 30000,
                    "employment_types": ["salaried", "self_employed"],
                    "age_range": [21, 70]
                },
                "processing_fee": "0.5% of loan amount",
                "prepayment_charges": "2% + applicable taxes"
            },
            "car_loan": {
                "name": "Car Loan",
                "min_amount": 100000,
                "max_amount": 10000000,
                "min_term_months": 12,
                "max_term_months": 84,
                "interest_rate_range": "7.35% - 12.35%",
                "eligibility_criteria": {
                    "min_cibil_score": 650,
                    "min_income_annum": 200000,
                    "max_loan_to_income_ratio": 3.0,
                    "min_bank_assets": 20000,
                    "employment_types": ["salaried", "self_employed"],
                    "age_range": [21, 65]
                },
                "processing_fee": "0.5% of loan amount",
                "prepayment_charges": "2.5% + applicable taxes"
            }
        }
    },
    "ICICI": {
        "name": "ICICI Bank",
        "loans": {
            "business_loan": {
                "name": "Business Loan",
                "min_amount": 50000,
                "max_amount": 5000000,
                "min_term_months": 12,
                "max_term_months": 120,
                "interest_rate_range": "12.50% - 18.50%",
                "eligibility_criteria": {
                    "min_cibil_score": 650,
                    "min_income_annum": 300000,
                    "max_loan_to_income_ratio": 3.0,
                    "min_bank_assets": 100000,
                    "employment_types": ["self_employed"],
                    "age_range": [21, 65],
                    "business_vintage_years": 2
                },
                "processing_fee": "1.5% of loan amount",
                "prepayment_charges": "3% + applicable taxes"
            }
        }
    }
}

def get_banks_list():
    """Get list of available banks"""
    return [{"id": bank_id, "name": bank_data["name"]}
            for bank_id, bank_data in BANK_LOAN_PRODUCTS.items()]

def get_bank_loans(bank_id):
    """Get loan products for a specific bank"""
    if bank_id not in BANK_LOAN_PRODUCTS:
        return None

    bank_data = BANK_LOAN_PRODUCTS[bank_id]
    loans = []

    for loan_id, loan_data in bank_data["loans"].items():
        loan_info = {
            "id": loan_id,
            "name": loan_data["name"],
            "amount_range": f"₹{loan_data['min_amount']:,} - ₹{loan_data['max_amount']:,}",
            "term_range": f"{loan_data['min_term_months']} - {loan_data['max_term_months']} months",
            "interest_rate": loan_data["interest_rate_range"],
            "processing_fee": loan_data["processing_fee"]
        }
        loans.append(loan_info)

    return {
        "bank_name": bank_data["name"],
        "loans": loans
    }

def get_loan_details(bank_id, loan_id):
    """Get detailed information about a specific loan product"""
    if bank_id not in BANK_LOAN_PRODUCTS:
        return None

    bank_data = BANK_LOAN_PRODUCTS[bank_id]
    if loan_id not in bank_data["loans"]:
        return None

    loan_data = bank_data["loans"][loan_id]

    return {
        "bank_name": bank_data["name"],
        "loan_name": loan_data["name"],
        "amount_range": {
            "min": loan_data["min_amount"],
            "max": loan_data["max_amount"]
        },
        "term_range": {
            "min_months": loan_data["min_term_months"],
            "max_months": loan_data["max_term_months"]
        },
        "interest_rate_range": loan_data["interest_rate_range"],
        "eligibility_criteria": loan_data["eligibility_criteria"],
        "processing_fee": loan_data["processing_fee"],
        "prepayment_charges": loan_data["prepayment_charges"]
    }