#!/usr/bin/env python
"""
Installation and setup guide for development
"""

import subprocess
import sys
import os
from pathlib import Path

def create_virtual_environment():
    """Create Python virtual environment"""
    print("Creating virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    print("✓ Virtual environment created")

def install_dependencies():
    """Install required packages"""
    print("\nInstalling dependencies...")
    
    if sys.platform == "win32":
        pip_cmd = "venv\\Scripts\\pip"
    else:
        pip_cmd = "venv/bin/pip"
    
    subprocess.check_call([pip_cmd, "install", "-r", "requirements.txt"])
    print("✓ Dependencies installed")

def create_directories():
    """Create necessary data directories"""
    print("\nCreating data directories...")
    
    dirs = [
        "data/raw",
        "data/processed",
        "models",
        "logs"
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created {dir_path}")

def run_tests():
    """Run unit tests"""
    print("\nRunning tests...")
    
    if sys.platform == "win32":
        pytest_cmd = "venv\\Scripts\\pytest"
    else:
        pytest_cmd = "venv/bin/pytest"
    
    try:
        subprocess.check_call([pytest_cmd, "tests/", "-v"])
        print("✓ All tests passed")
    except subprocess.CalledProcessError:
        print("✗ Some tests failed")

def main():
    """Main setup function"""
    print("="*50)
    print("AI-Driven Loan Approval Prediction System Setup")
    print("="*50)
    
    try:
        create_virtual_environment()
        install_dependencies()
        create_directories()
        
        print("\n" + "="*50)
        print("Setup completed successfully!")
        print("="*50)
        
        print("\nNext steps:")
        print("1. Activate virtual environment:")
        if sys.platform == "win32":
            print("   venv\\Scripts\\activate")
        else:
            print("   source venv/bin/activate")
        
        print("\n2. Run tests:")
        print("   pytest tests/ -v")
        
        print("\n3. Start API server:")
        print("   python src/api/app.py")
        
        print("\n4. Start Jupyter notebook:")
        print("   jupyter notebook")
        
    except Exception as e:
        print(f"\n✗ Setup failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
