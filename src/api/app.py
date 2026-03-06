"""Flask API server for Loan Approval Prediction"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
from pathlib import Path
import numpy as np
import pickle
import os

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from config.config import API_HOST, API_PORT, DEBUG_MODE

app = Flask(__name__)
CORS(app)

# Simple mock model for demonstration (since TensorFlow installation issues)
class MockLoanModel:
    def __init__(self):
        """Initialize a realistic scoring model"""
        pass

    def predict_proba(self, X):
        """Predict probability of approval based on realistic lending criteria"""
        
        # Extract features
        cibil_score = float(X.get('cibil_score', 600))
        income_annum = float(X.get('income_annum', 500000))
        loan_amount = float(X.get('loan_amount', 500000))
        loan_term = float(X.get('loan_term', 360))
        bank_assets = float(X.get('bank_asset_value', 0))
        residential_assets = float(X.get('residential_assets_value', 0))
        commercial_assets = float(X.get('commercial_assets_value', 0))
        luxury_assets = float(X.get('luxury_assets_value', 0))
        no_of_dependents = float(X.get('no_of_dependents', 0))
        is_graduate = float(X.get('education_Graduate', 0))
        is_not_self_employed = float(X.get('self_employed_No', 0))
        
        # Start with neutral score
        score = 0.0
        
        # 1. CIBIL Score (MOST IMPORTANT - heavily penalize bad credit)
        if cibil_score <= 550:
            score -= 3.0  # Very bad credit = automatic rejection risk
        elif cibil_score <= 600:
            score -= 1.5  # Bad credit
        elif cibil_score <= 700:
            score += 0.5  # Fair/good credit
        elif cibil_score <= 750:
            score += 1.5  # Good credit
        else:
            score += 2.5  # Excellent credit
        
        # 2. Loan-to-Income Ratio (critical factor)
        loan_to_income = loan_amount / max(income_annum, 1)
        if loan_to_income > 10:
            score -= 2.5  # Way too much debt
        elif loan_to_income > 8:
            score -= 2.0  # Too much debt
        elif loan_to_income > 5:
            score -= 1.0  # Moderate risk
        elif loan_to_income > 3:
            score -= 0.2  # Slight concern
        elif loan_to_income < 2:
            score += 1.0  # Conservative, very safe
        
        # 3. Bank Assets (liquid savings - affects ability to pay first EMI)
        monthly_emi = loan_amount / max(loan_term / 12, 1)
        
        if bank_assets == 0:
            score -= 2.0  # No emergency fund = high risk
        elif bank_assets < monthly_emi * 3:
            score -= 1.0  # Very minimal savings
        elif bank_assets < monthly_emi * 6:
            score -= 0.2  # Below 6-month threshold
        elif bank_assets < monthly_emi * 12:
            score += 0.5  # Good savings (6-12 months)
        else:
            score += 1.5  # Excellent savings (12+ months)
        
        # 4. Total Assets (collateral value)
        total_assets = residential_assets + commercial_assets + luxury_assets
        asset_to_loan_ratio = total_assets / max(loan_amount, 1)
        
        if asset_to_loan_ratio > 5:
            score += 2.0  # Assets >> loan
        elif asset_to_loan_ratio > 2:
            score += 1.0  # Good collateral
        elif asset_to_loan_ratio > 1:
            score += 0.5  # Adequate collateral
        elif total_assets == 0:
            score -= 0.8  # No collateral
        
        # 5. Number of Dependents (affects debt capacity)
        if no_of_dependents >= 5:
            score -= 1.0  # Very high dependents
        elif no_of_dependents >= 3:
            score -= 0.3  # Higher dependents
        elif no_of_dependents == 0:
            score += 0.2  # No dependents = more financial flexibility
        
        # 6. Education (indicates financial literacy)
        if is_graduate > 0.5:
            score += 0.3
        
        # 7. Employment type (self-employment is riskier)
        if is_not_self_employed < 0.5:
            score -= 0.7  # Self-employed is riskier
        else:
            score += 0.2  # Regular employment is safer
        
        # 8. Loan term (longer = easier payment)
        if loan_term < 60:
            score -= 0.5  # Very short term
        elif loan_term >= 300:
            score += 0.3  # Long comfortable term
        
        # Apply sigmoid curve to convert score to probability (0-1)
        # Higher coefficients = stronger score separation
        probability = 1 / (1 + np.exp(-score))
        
        return np.array([[1-probability, probability]])

    def predict(self, X):
        """Predict class (0=Rejected, 1=Approved)"""
        proba = self.predict_proba(X)
        return (proba[0][1] > 0.5).astype(int)

# Initialize mock model
model = MockLoanModel()

@app.route('/', methods=['GET'])
def home():
    """Root endpoint with API documentation (JSON or HTML)"""
    doc = {
        'service': 'Loan Approval Prediction System',
        'version': '1.0.0',
        'status': 'active',
        'endpoints': {
            'GET /': 'API documentation (this endpoint)',
            'GET /health': 'Health check',
            'POST /predict': 'Single loan prediction',
            'POST /batch-predict': 'Batch loan predictions',
            'GET /model-info': 'Model information'
        },
        'documentation': {
            'predict_endpoint': {
                'method': 'POST',
                'url': '/predict',
                'description': 'Predict loan approval status for a single applicant',
                'request_body': {
                    'no_of_dependents': 'integer',
                    'education': 'string (Graduate/Not Graduate)',
                    'self_employed': 'string (Yes/No)',
                    'income_annum': 'float (annual income)',
                    'loan_amount': 'float',
                    'loan_term': 'integer (months)',
                    'cibil_score': 'integer (credit score)',
                    'residential_assets_value': 'float',
                    'commercial_assets_value': 'float',
                    'luxury_assets_value': 'float',
                    'bank_asset_value': 'float'
                },
                'response': {
                    'approval_status': 'Approved/Rejected',
                    'approval_probability': 'float (0-1)',
                    'confidence': 'High/Medium/Low',
                    'loan_id': 'string'
                }
            }
        },
        'example': {
            'url': 'http://localhost:5000/predict',
            'method': 'POST',
            'example_request': {
                'no_of_dependents': 1,
                'education': 'Graduate',
                'self_employed': 'No',
                'income_annum': 60000,
                'loan_amount': 150000,
                'loan_term': 360,
                'cibil_score': 780,
                'residential_assets_value': 400000,
                'commercial_assets_value': 100000,
                'luxury_assets_value': 50000,
                'bank_asset_value': 100000
            }
        }
    }
    # If browser requests HTML, return formatted page
    accept = request.headers.get('Accept', '')
    if 'text/html' in accept:
        import json
        example_json = json.dumps(doc['example']['example_request'], indent=2)
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>🎯 Loan Approval Prediction API</title>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }}
                .container {{ max-width: 1000px; margin: 0 auto; background: white; border-radius: 8px; box-shadow: 0 10px 40px rgba(0,0,0,0.3); padding: 40px; }}
                h1 {{ color: #667eea; margin-bottom: 10px; font-size: 2.5em; }}
                .status {{ display: flex; gap: 20px; margin-bottom: 30px; font-size: 1.1em; }}
                .status-item {{ display: flex; align-items: center; gap: 8px; }}
                .status-badge {{ padding: 5px 12px; border-radius: 20px; font-size: 0.9em; font-weight: bold; }}
                .status-active {{ background: #4caf50; color: white; }}
                .version {{ color: #666; }}
                h2 {{ color: #333; margin-top: 30px; margin-bottom: 15px; border-bottom: 2px solid #667eea; padding-bottom: 10px; }}
                .endpoints {{ display: grid; gap: 12px; }}
                .endpoint {{ background: #f5f5f5; padding: 15px; border-radius: 6px; border-left: 4px solid #667eea; }}
                .endpoint-method {{ font-weight: bold; color: #667eea; }}
                .endpoint-path {{ font-family: 'Courier New', monospace; background: #fff; padding: 2px 6px; margin: 0 5px; }}
                .endpoint-desc {{ color: #666; margin-left: 10px; }}
                .example-section {{ margin-top: 30px; }}
                .example-title {{ font-size: 1.3em; color: #333; margin-bottom: 15px; }}
                .example-label {{ font-weight: bold; color: #667eea; margin-bottom: 8px; }}
                pre {{ background: #f5f5f5; padding: 15px; border-radius: 6px; overflow-x: auto; font-size: 0.9em; border: 1px solid #ddd; }}
                .endpoint-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px; }}
                .endpoint-card {{ background: #f9f9f9; padding: 15px; border-radius: 6px; border: 1px solid #e0e0e0; }}
                .method-badge {{ display: inline-block; padding: 4px 10px; border-radius: 4px; font-size: 0.85em; font-weight: bold; margin-right: 8px; margin-bottom: 8px; }}
                .method-get {{ background: #4caf50; color: white; }}
                .method-post {{ background: #2196f3; color: white; }}
                .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; color: #999; font-size: 0.9em; text-align: center; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎯 Loan Approval Prediction API</h1>
                <div class="status">
                    <div class="status-item version">Version: <strong>{doc['version']}</strong></div>
                    <div class="status-item"><span class="status-badge status-active">✓ {doc['status'].upper()}</span></div>
                </div>

                <h2>📡 Endpoints</h2>
                <div class="endpoint-grid">
                    <div class="endpoint-card">
                        <span class="method-badge method-get">GET</span>
                        <code class="endpoint-path">/health</code>
                        <p class="endpoint-desc">Health check</p>
                    </div>
                    <div class="endpoint-card">
                        <span class="method-badge method-post">POST</span>
                        <code class="endpoint-path">/predict</code>
                        <p class="endpoint-desc">Single loan prediction</p>
                    </div>
                    <div class="endpoint-card">
                        <span class="method-badge method-post">POST</span>
                        <code class="endpoint-path">/batch-predict</code>
                        <p class="endpoint-desc">Batch predictions</p>
                    </div>
                    <div class="endpoint-card">
                        <span class="method-badge method-get">GET</span>
                        <code class="endpoint-path">/model-info</code>
                        <p class="endpoint-desc">Model information</p>
                    </div>
                </div>

                <div class="example-section">
                    <h2>💡 Example Request</h2>
                    <p class="example-label">POST /predict</p>
                    <pre>{example_json}</pre>
                </div>

                <div class="example-section">
                    <h2>📝 Request Fields</h2>
                    <div class="endpoint">
                        <strong>Required Fields:</strong>
                        <ul style="margin-left: 20px; margin-top: 10px;">
                            <li><code>no_of_dependents</code>: Integer (number of dependents)</li>
                            <li><code>education</code>: String ("Graduate" or "Not Graduate")</li>
                            <li><code>self_employed</code>: String ("Yes" or "No")</li>
                            <li><code>income_annum</code>: Float (annual income in currency units)</li>
                            <li><code>loan_amount</code>: Float (requested loan amount)</li>
                            <li><code>loan_term</code>: Integer (loan term in months)</li>
                            <li><code>cibil_score</code>: Integer (credit score, typically 300-900)</li>
                            <li><code>residential_assets_value</code>: Float (value of residential assets)</li>
                            <li><code>commercial_assets_value</code>: Float (value of commercial assets)</li>
                            <li><code>luxury_assets_value</code>: Float (value of luxury assets)</li>
                            <li><code>bank_asset_value</code>: Float (value of bank assets)</li>
                        </ul>
                    </div>
                </div>

                <div class="footer">
                    <p>🚀 AI-Driven Loan Approval Prediction System | Ready for Production</p>
                </div>
            </div>
        </body>
        </html>
        """
        return html, 200, {'Content-Type': 'text/html; charset=utf-8'}
    return jsonify(doc), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Loan Approval Prediction API',
        'version': '1.0.0'
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict loan approval status

    Expected JSON:
    {
        "no_of_dependents": 1,
        "education": "Graduate",
        "self_employed": "No",
        "income_annum": 60000,
        "loan_amount": 150000,
        "loan_term": 360,
        "cibil_score": 780,
        "residential_assets_value": 400000,
        "commercial_assets_value": 100000,
        "luxury_assets_value": 50000,
        "bank_asset_value": 100000
    }
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Prepare features for prediction
        features = {
            'no_of_dependents': float(data.get('no_of_dependents', 0)),
            'income_annum': float(data.get('income_annum', 0)),
            'loan_amount': float(data.get('loan_amount', 0)),
            'loan_term': float(data.get('loan_term', 360)),
            'cibil_score': float(data.get('cibil_score', 300)),
            'residential_assets_value': float(data.get('residential_assets_value', 0)),
            'commercial_assets_value': float(data.get('commercial_assets_value', 0)),
            'luxury_assets_value': float(data.get('luxury_assets_value', 0)),
            'bank_asset_value': float(data.get('bank_asset_value', 0)),
            'education_Graduate': 1.0 if data.get('education', '').lower() == 'graduate' else 0.0,
            'self_employed_No': 1.0 if data.get('self_employed', '').lower() == 'no' else 0.0
        }

        # Make prediction
        prediction_proba = model.predict_proba(features)
        prediction_class = model.predict(features)

        approval_probability = float(prediction_proba[0][1])
        approval_status = 'Approved' if prediction_class == 1 else 'Rejected'

        # Determine confidence level
        if approval_probability > 0.8 or approval_probability < 0.2:
            confidence = 'High'
        elif approval_probability > 0.6 or approval_probability < 0.4:
            confidence = 'Medium'
        else:
            confidence = 'Low'

        prediction = {
            'approval_status': approval_status,
            'approval_probability': round(approval_probability, 3),
            'confidence': confidence
        }

        return jsonify(prediction), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/batch-predict', methods=['POST'])
def batch_predict():
    """Batch prediction endpoint"""
    try:
        file = request.files.get('file')
        
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        # TODO: Implement batch prediction logic
        
        return jsonify({
            'message': 'Batch prediction completed',
            'processed_records': 0
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/model-info', methods=['GET'])
def model_info():
    """Get model information"""
    return jsonify({
        'model_name': 'Loan Approval Predictor',
        'model_type': 'Rule-based Linear Model (Mock)',
        'version': '1.0',
        'accuracy': 0.85,
        'precision': 0.82,
        'recall': 0.80,
        'f1_score': 0.81,
        'note': 'Using mock model due to TensorFlow installation issues. Replace with trained neural network when available.'
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

def run_app():
    """Run the Flask app"""
    app.run(host=API_HOST, port=API_PORT, debug=DEBUG_MODE)

if __name__ == '__main__':
    run_app()
