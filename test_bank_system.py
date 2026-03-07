#!/usr/bin/env python3
"""
Test script for the new Bank-Specific Loan Eligibility System
"""

import requests
import json

def test_bank_loan_system():
    """Test the complete bank loan eligibility system"""

    print("🏦 Testing Bank-Specific Loan Eligibility System")
    print("=" * 60)

    # Test 1: Get available banks
    print("\n1. Getting available banks...")
    try:
        response = requests.get('http://localhost:5000/banks')
        banks_data = response.json()
        print(f"✅ Found {banks_data['total_banks']} banks:")
        for bank in banks_data['banks']:
            print(f"   - {bank['name']} ({bank['id']})")
    except Exception as e:
        print(f"❌ Failed to get banks: {e}")
        return

    # Test 2: Get loans for SBI
    print("\n2. Getting loan products for SBI...")
    try:
        response = requests.get('http://localhost:5000/banks/SBI/loans')
        sbi_loans = response.json()
        print(f"✅ SBI offers {len(sbi_loans['loans'])} loan products:")
        for loan in sbi_loans['loans']:
            print(f"   - {loan['name']} ({loan['id']})")
            print(f"     Amount: {loan['amount_range']}")
            print(f"     Interest: {loan['interest_rate']}")
    except Exception as e:
        print(f"❌ Failed to get SBI loans: {e}")
        return

    # Test 3: Get loan details
    print("\n3. Getting details for SBI Home Loan...")
    try:
        response = requests.get('http://localhost:5000/banks/SBI/loans/home_loan')
        loan_details = response.json()
        print("✅ Home Loan Details:")
        print(f"   Bank: {loan_details['bank_name']}")
        print(f"   Loan: {loan_details['loan_name']}")
        print(f"   Amount Range: ₹{loan_details['amount_range']['min']:,} - ₹{loan_details['amount_range']['max']:,}")
        print(f"   Interest Rate: {loan_details['interest_rate_range']}")
        print(f"   Min CIBIL Score: {loan_details['eligibility_criteria']['min_cibil_score']}")
    except Exception as e:
        print(f"❌ Failed to get loan details: {e}")
        return

    # Test 4: Test loan eligibility prediction
    print("\n4. Testing loan eligibility prediction...")

    # Test case 1: Good applicant
    good_applicant = {
        "bank_id": "SBI",
        "loan_id": "home_loan",
        "user_data": {
            "no_of_dependents": 1,
            "education": "Graduate",
            "self_employed": "No",
            "income_annum": 800000,
            "loan_amount": 2000000,
            "loan_term": 240,
            "cibil_score": 780,
            "residential_assets_value": 1500000,
            "commercial_assets_value": 500000,
            "luxury_assets_value": 200000,
            "bank_asset_value": 150000
        }
    }

    try:
        response = requests.post('http://localhost:5000/predict-loan-eligibility',
                               json=good_applicant)
        result = response.json()
        print("✅ Good Applicant Result:")
        print(f"   Status: {result['eligibility_status']}")
        print(f"   Score: {result['eligibility_score']}%")
        print(f"   Confidence: {result['confidence']}")
        print(f"   Top Reasons: {result['reasons'][:2]}")
    except Exception as e:
        print(f"❌ Failed eligibility prediction: {e}")
        return

    # Test case 2: Poor applicant
    poor_applicant = {
        "bank_id": "SBI",
        "loan_id": "home_loan",
        "user_data": {
            "no_of_dependents": 3,
            "education": "Not Graduate",
            "self_employed": "Yes",
            "income_annum": 200000,
            "loan_amount": 3000000,
            "loan_term": 360,
            "cibil_score": 550,
            "residential_assets_value": 0,
            "commercial_assets_value": 0,
            "luxury_assets_value": 0,
            "bank_asset_value": 5000
        }
    }

    try:
        response = requests.post('http://localhost:5000/predict-loan-eligibility',
                               json=poor_applicant)
        result = response.json()
        print("\n✅ Poor Applicant Result:")
        print(f"   Status: {result['eligibility_status']}")
        print(f"   Score: {result['eligibility_score']}%")
        print(f"   Confidence: {result['confidence']}")
        print(f"   Top Reasons: {result['reasons'][:2]}")
    except Exception as e:
        print(f"❌ Failed eligibility prediction: {e}")
        return

    print("\n🎉 All tests completed successfully!")
    print("\n📱 Access the enhanced frontend at: http://localhost:3000")
    print("🔧 API Documentation at: http://localhost:5000")

if __name__ == '__main__':
    test_bank_loan_system()