# GitHub Setup Instructions

## Why Personal Access Token?

For **team collaboration**, Personal Access Tokens (PAT) are **recommended** over passwords because they:
- ✅ Allow fine-grained access control
- ✅ Can be revoked independently per user
- ✅ Work seamlessly with Git Credential Manager on Windows
- ✅ Are more secure than storing plain passwords
- ✅ Support 2FA and advanced security features

## Step 1: Create a Personal Access Token

1. Go to **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. Click **Generate new token (classic)**
3. **Name**: `loan-prediction-system`
4. **Expiration**: 90 days (or as your team policy requires)
5. **Select scopes**: Check these boxes:
   - `repo` (Full control of private repositories)
   - `workflow` (Update GitHub Action workflows)
   - `write:packages` (Upload packages to GitHub Package Registry)
6. Click **Generate token** at the bottom
7. **⚠️ Copy the token immediately** - you won't be able to see it again!

## Step 2: Configure Git Credential Manager

When you try to push, Git will prompt you:

**In PowerShell:**
```
Username for 'https://github.com': your-github-username
Password for 'https://github.com/your-username': <paste-your-token-here>
```

**Then select:**
- ✅ Store credentials in Windows Credential Manager
- This saves your token securely so you don't need to enter it again

## Step 3: Push Your Code

After setting up the token, run:

```powershell
cd "c:\Users\bhava\loan-approval-prediction-system\deep-learning-loan-prediction-system--1"
git push -u origin main
```

When prompted, use:
- **Username**: Your GitHub username (e.g., `chereddylakshmibhavana`)
- **Password**: Your Personal Access Token (not your GitHub password)

## Step 4: Verify

Once pushed, you should see:
```
Branch 'main' set up to track remote origin/main'.
```

## If It Still Fails...

### Option A: Collaborator Access
Ask **ChereddyLakshmiBhavana** (repo owner) to:
1. Go to repository → Settings → Collaborators
2. Add your GitHub username: `chereddylakshmibhavana`
3. You'll receive an invite - accept it
4. Then retry the push

### Option B: Open Source Alternative
If you don't have access rights, you can:
1. Fork the repository to your account
2. Push your changes
3. Create a Pull Request for the main repo

## For Your Team

**Share this setup process with all team members:**
1. Each person gets their own Personal Access Token
2. Tokens are stored securely in Windows Credential Manager
3. Tokens can be revoked independently
4. No passwords are shared

## Token Security Tips

- ⚠️ **Never commit or share tokens** in code
- 🔄 **Rotate tokens periodically** (recommend every 90 days)
- 🗑️ **Revoke tokens** when team members leave
- 📝 **Document who has tokens** for audit purposes
- 🔐 **Use environment variables** for CI/CD, not hardcoded tokens
