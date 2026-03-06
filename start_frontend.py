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
    frontend_path = Path(__file__).parent / 'frontend' / 'index.html'
    with open(frontend_path, 'r', encoding='utf-8') as f:
        return f.read()

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