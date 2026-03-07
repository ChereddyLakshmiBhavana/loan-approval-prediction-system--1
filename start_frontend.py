#!/usr/bin/env python3
"""
Start only the Frontend Web Server
Runs on http://localhost:3000
"""

import sys
from pathlib import Path
from flask import Flask
import os

app = Flask(__name__, static_folder='frontend')

# Serve the frontend
@app.route('/')
def serve_frontend():
    """Serve the main frontend application"""
    frontend_path = Path(__file__).parent / 'frontend' / 'bank_loan_eligibility.html'
    print(f"DEBUG: Serving file from: {frontend_path}")
    print(f"DEBUG: File exists: {frontend_path.exists()}")
    with open(frontend_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"DEBUG: Content length: {len(content)}")
        print(f"DEBUG: First 100 chars: {content[:100]}")
        return content

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    from flask import send_from_directory
    return send_from_directory(Path(__file__).parent / 'frontend', filename)

if __name__ == '__main__':
    print("🌐 Starting Frontend Web Server...")
    print("📍 Running on http://localhost:3000")
    print()
    print("✨ Make sure the Backend API is running on http://localhost:5000")
    print()
    print("Press Ctrl+C to stop")
    print()
    app.run(host='0.0.0.0', port=3000, debug=True)