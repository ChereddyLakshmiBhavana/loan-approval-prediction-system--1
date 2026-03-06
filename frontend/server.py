from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__, static_folder='../frontend')

# Serve the frontend
@app.route('/')
def serve_frontend():
    """Serve the main frontend application"""
    frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'index.html')
    with open(frontend_path, 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files if needed"""
    return send_from_directory(os.path.join(os.path.dirname(__file__), '..', 'frontend'), filename)

if __name__ == '__main__':
    print("🚀 Frontend server starting on http://localhost:3000")
    print("📱 Access the loan prediction app in your browser")
    app.run(host='0.0.0.0', port=3000, debug=True)