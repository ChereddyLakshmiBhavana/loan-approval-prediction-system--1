#!/usr/bin/env python3
"""
Repository Access Setup - This script verifies and handles access permissions
"""

import subprocess
import sys
from pathlib import Path

def check_git_config():
    """Check current git configuration"""
    print("=" * 60)
    print("CHECKING GIT CONFIGURATION")
    print("=" * 60)
    
    try:
        result = subprocess.run(['git', 'config', '--get', 'remote.origin.url'], 
                              capture_output=True, text=True, check=True)
        print(f"✓ Remote URL: {result.stdout.strip()}")
    except subprocess.CalledProcessError:
        print("✗ No remote configured")
        return False
    
    return True

def check_github_access():
    """Check if we have push access"""
    print("\n" + "=" * 60)
    print("CHECKING GITHUB ACCESS")
    print("=" * 60)
    
    # Try a dry-run push to see if we have access
    result = subprocess.run(
        ['git', 'push', '--dry-run', 'origin', 'main'],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✓ Push access verified!")
        return True
    else:
        print("✗ Push access denied")
        print(f"  Error: {result.stderr.strip()}")
        return False

def show_collaborator_instructions():
    """Show instructions for repo owner to add collaborator"""
    print("\n" + "=" * 60)
    print("GETTING COLLABORATOR ACCESS")
    print("=" * 60)
    print("""
TO GET PUSH ACCESS, THE REPOSITORY OWNER MUST:

1. Go to: https://github.com/hemalatha1311/deep-learning-loan-prediction-system-
2. Click "Settings" tab
3. Click "Collaborators" (left sidebar)
4. Click "Add people"
5. Search for: cheredddylakshmibhavana25
6. Select the username and click "Add {username} to this repository"
7. Choose permission level: "Write" (to push code)
8. Click "Add"

ONCE ADDED:
- You'll receive an invitation
- Accept the invitation
- Run this script again to verify access
- Then run: git push -u origin main
""")

def attempt_push():
    """Attempt to push if access is available"""
    print("\n" + "=" * 60)
    print("ATTEMPTING TO PUSH CHANGES")
    print("=" * 60)
    
    result = subprocess.run(
        ['git', 'push', '-u', 'origin', 'main'],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✓ Successfully pushed to GitHub!")
        print(result.stdout)
        return True
    else:
        print("✗ Push failed")
        print(result.stderr)
        return False

def main():
    """Main workflow"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  AI-DRIVEN LOAN APPROVAL PREDICTION SYSTEM  ".center(58) + "║")
    print("║" + "  GitHub Repository Setup  ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    # Check git config
    if not check_git_config():
        print("\n✗ Git not properly configured")
        sys.exit(1)
    
    # Check access
    has_access = check_github_access()
    
    if not has_access:
        show_collaborator_instructions()
        print("\n📋 AFTER BEING ADDED AS COLLABORATOR:")
        print("   1. Accept the invitation email from GitHub")
        print("   2. Run this script again")
        print("   3. Your code will be pushed automatically")
        sys.exit(1)
    
    # If we have access, try to push
    if attempt_push():
        print("\n✅ All done! Your project is now on GitHub.")
        print("   Team members can clone it with:")
        print("   git clone https://github.com/hemalatha1311/deep-learning-loan-prediction-system-.git")
        sys.exit(0)
    else:
        print("\n⚠️  Push failed. Please check:")
        print("   1. You're connected to the internet")
        print("   2. Your GitHub credentials are correct")
        print("   3. You have write access (check collaborators)")
        sys.exit(1)

if __name__ == '__main__':
    main()
