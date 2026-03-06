# Frontend - Loan Approval Prediction System

A modern, responsive web interface for the AI-powered loan approval prediction system.

## Features

- 🎨 Modern, professional UI with gradient design
- 📱 Fully responsive (works on mobile and desktop)
- ⚡ Real-time API integration with backend
- 🎯 Visual probability indicators
- 🔄 Loading states and error handling
- 📊 Confidence level display

## Quick Start

1. **Start the Backend API first:**
   ```bash
   cd src/api
   python app.py
   ```
   Backend will run on http://localhost:5000

2. **Start the Frontend:**
   ```bash
   cd frontend
   python server.py
   ```
   Frontend will run on http://localhost:3000

3. **Open your browser** and go to http://localhost:3000

## Form Fields

The application collects the following information for loan prediction:

- **Number of Dependents**: Family size (0-10)
- **Education**: Graduate/Not Graduate
- **Self Employed**: Yes/No
- **Annual Income**: Applicant's yearly income in ₹
- **Loan Amount**: Requested loan amount in ₹
- **Loan Term**: Duration in months (12-360)
- **CIBIL Score**: Credit score (300-900)
- **Asset Values**: Residential, Commercial, Luxury, and Bank assets in ₹

## API Integration

The frontend communicates with the backend API at `/predict` endpoint with POST requests containing JSON data.

## Technologies Used

- HTML5, CSS3, JavaScript (ES6+)
- Flask (Python web server)
- Responsive design with CSS Grid
- Modern UI with gradients and animations