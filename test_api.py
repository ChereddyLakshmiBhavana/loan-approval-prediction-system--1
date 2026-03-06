#!/usr/bin/env python3
"""Test the API to verify prediction variation"""

import requests
import json

endpoint = "http://127.0.0.1:5000/predict"

# Good applicant
good_data = {
    "no_of_dependents": 1,
    "education": "Graduate",
    "self_employed": "No",
    "income_annum": 1000000,
    "loan_amount": 200000,
    "loan_term": 360,
    "cibil_score": 800,
    "residential_assets_value": 5000000,
    "commercial_assets_value": 0,
    "luxury_assets_value": 0,
    "bank_asset_value": 500000
}

# Poor applicant  
poor_data = {
    "no_of_dependents": 3,
    "education": "Not Graduate",
    "self_employed": "Yes",
    "income_annum": 300000,
    "loan_amount": 500000,
    "loan_term": 360,
    "cibil_score": 550,
    "residential_assets_value": 0,
    "commercial_assets_value": 0,
    "luxury_assets_value": 50000,
    "bank_asset_value": 5000
}

print("=" * 60)
print("Testing Loan Prediction API - Verification")
print("=" * 60)

try:
    # Test good applicant
    print("\n[GOOD APPLICANT]")
    print("Profile: High income ($1M), Excellent CIBIL (800), Good savings ($500K), Significant assets ($5M)")
    r1 = requests.post(endpoint, json=good_data, timeout=5)
    if r1.status_code == 200:
        result1 = r1.json()
        print(f"Approval Probability: {result1['approval_probability']:.4f} ({result1['approval_probability']*100:.1f}%)")
        print(f"Status: {result1['approval_status']}")
        print(f"Confidence: {result1['confidence']}")
    else:
        print(f"ERROR: HTTP {r1.status_code}")
        print(result1)
    
    # Test poor applicant
    print("\n[POOR APPLICANT]")
    print("Profile: Lower income ($300K), Poor CIBIL (550), Minimal savings ($5K), No significant assets")
    r2 = requests.post(endpoint, json=poor_data, timeout=5)
    if r2.status_code == 200:
        result2 = r2.json()
        print(f"Approval Probability: {result2['approval_probability']:.4f} ({result2['approval_probability']*100:.1f}%)")
        print(f"Status: {result2['approval_status']}")
        print(f"Confidence: {result2['confidence']}")
    else:
        print(f"ERROR: HTTP {r2.status_code}")
        print(result2)
    
    # Summary
    print("\n" + "=" * 60)
    prob_diff = abs(result1['approval_probability'] - result2['approval_probability'])
    print(f"Probability Difference: {prob_diff:.4f}")
    
    if prob_diff > 0.5:
        print("✅ SUCCESS: Model is showing proper variation!")
        print(f"   Good applicant: {result1['approval_probability']:.1%}")
        print(f"   Poor applicant: {result2['approval_probability']:.1%}")
    else:
        print("❌ FAILED: Model predictions too similar")
        print(f"   Good applicant: {result1['approval_probability']:.1%}")
        print(f"   Poor applicant: {result2['approval_probability']:.1%}")
    print("=" * 60)
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
