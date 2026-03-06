#!/usr/bin/env python3
"""
Start only the Backend API Server
Runs on http://localhost:5000
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from api.app import app
from config.config import API_HOST, API_PORT, DEBUG_MODE

print("🚀 Starting Backend API Server...")
print(f"📍 Running on http://localhost:{API_PORT}")
print()
print("API Endpoints:")
print("  GET  /health        - Health check")
print("  POST /predict       - Single prediction")
print("  GET  /model-info    - Model information")
print()
print("Press Ctrl+C to stop")
print()

app.run(host=API_HOST, port=API_PORT, debug=DEBUG_MODE)