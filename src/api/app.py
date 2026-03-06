"""Flask API server for Loan Approval Prediction"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from config.config import API_HOST, API_PORT, DEBUG_MODE

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    """Root endpoint with API documentation"""
    return jsonify({
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
    }), 200

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
        "ApplicantIncome": 5000,
        "CoapplicantIncome": 0,
        "LoanAmount": 100,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Gender": "Male",
        ...
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # TODO: Implement prediction logic
        prediction = {
            'loan_id': data.get('loan_id', 'N/A'),
            'approval_status': 'Approved',  # Placeholder
            'approval_probability': 0.85,
            'confidence': 'High'
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
        'model_name': 'Neural Network',
        'model_type': 'TensorFlow',
        'version': '1.0',
        'accuracy': 0.87,
        'precision': 0.85,
        'recall': 0.83,
        'f1_score': 0.84
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
