#!/usr/bin/env python3
"""
🚀 Loan Approval Prediction System - Complete Application Launcher

This script starts both the backend API and frontend servers simultaneously.
Perfect for hackathon demonstrations and development.

Usage:
    python run_complete_system.py

This will start:
- Backend API on http://localhost:5000
- Frontend on http://localhost:3000

Press Ctrl+C to stop both servers.
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def run_command(command, cwd=None, name=""):
    """Run a command in background and return the process"""
    print(f"🚀 Starting {name}...")
    return subprocess.Popen(
        command,
        shell=True,
        cwd=cwd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def main():
    print("🎯 LOAN APPROVAL PREDICTION SYSTEM")
    print("=" * 50)
    print("Starting complete application (Backend + Frontend)")
    print()

    # Get project root
    project_root = Path(__file__).parent

    # Use the virtual environment Python executable
    python_exe = str(project_root / '.venv' / 'Scripts' / 'python.exe')

    # Backend command
    backend_cmd = f'"{python_exe}" src/api/app.py'
    backend_cwd = project_root

    # Frontend command
    frontend_cmd = f'"{python_exe}" frontend/server.py'
    frontend_cwd = project_root

    backend_process = None
    frontend_process = None

    try:
        # Start backend
        backend_process = run_command(backend_cmd, str(backend_cwd), "Backend API on port 5000")
        
        # Wait for backend to start
        time.sleep(4)

        # Start frontend
        frontend_process = run_command(frontend_cmd, str(frontend_cwd), "Frontend Server on port 3000")

        # Wait for frontend to start
        time.sleep(2)

        print()
        print("✅ SERVERS STARTED SUCCESSFULLY!")
        print("=" * 50)
        print("🌐 Frontend: http://localhost:3000 (Main Application)")
        print("🔧 Backend API: http://localhost:5000 (API Documentation)")
        print()
        print("📱 Open http://localhost:3000 in your browser to use the app")
        print("📚 Visit http://localhost:5000 for API documentation")
        print()
        print("⏸️  Press Ctrl+C to stop both servers...")
        print()

        # Keep running until user interrupts
        while True:
            time.sleep(1)
            
            # Check if processes are still alive
            if backend_process and backend_process.poll() is not None:
                print("⚠️  Backend API crashed!")
            if frontend_process and frontend_process.poll() is not None:
                print("⚠️  Frontend server crashed!")

    except KeyboardInterrupt:
        print()
        print("🛑 Shutting down servers...")

        # Terminate processes gracefully
        if backend_process and backend_process.poll() is None:
            backend_process.terminate()
            try:
                backend_process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                backend_process.kill()

        if frontend_process and frontend_process.poll() is None:
            frontend_process.terminate()
            try:
                frontend_process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                frontend_process.kill()

        print("✅ All servers stopped. Goodbye! 👋")

    except Exception as e:
        print(f"❌ Error: {e}")
        if backend_process:
            backend_process.kill()
        if frontend_process:
            frontend_process.kill()
        sys.exit(1)

if __name__ == "__main__":
    main()