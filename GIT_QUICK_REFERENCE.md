# 🔖 Git & GitHub Quick Reference (Save This!)

## Essential Commands (All You Really Need)

### Setup (One time)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"
```

### Start a Project
```bash
mkdir my-project
cd my-project
git init
```

### Everyday Workflow
```bash
# 1. Check what changed
git status

# 2. Stage all changes
git add .

# 3. Save with message
git commit -m "What you changed"

# 4. Upload to GitHub
git push origin main
```

### First Time Setup with GitHub
```bash
# Create repo on github.com first, then run:
git remote add origin https://github.com/USERNAME/repo-name.git
git branch -M main
git push -u origin main
```

---

## All Git Commands (Organized by Use)

### See What Changed
```bash
git status              # What's different?
git diff                # What lines changed?
git log                 # What commits were made?
git log --oneline       # Short commit history
git show COMMIT_ID      # See one commit
```

### Undo Changes
```bash
git add .                          # Oh no, undo staging
git reset HEAD filename.py         # Unstage one file
git checkout -- filename.py        # Undo all changes to one file
git revert HEAD                    # Undo last commit (safe)
git reset HEAD~1                   # Delete last commit (risky!)
```

### Branches (for advanced work)
```bash
git branch                         # See branches
git branch new-feature             # Create new branch
git checkout new-feature           # Switch branch
git checkout -b new-feature        # Create + switch
git merge new-feature              # Merge branch to main
```

### Remote (GitHub)
```bash
git remote -v                      # See GitHub links
git pull origin main               # Get latest from GitHub
git push origin main               # Send to GitHub
git fetch origin                   # Download new data (don't merge yet)
git clone URL                      # Copy someone else's repo
```

---

## Commit Message Best Practices

### Good Examples
```bash
git commit -m "Add: customer data preprocessing function"
git commit -m "Fix: handle missing values in age column"
git commit -m "Improve: reduce model training time by 30%"
git commit -m "Docs: update README with installation steps"
git commit -m "Refactor: reorganize code into modules"
```

### Bad Examples (Don't do this!)
```bash
git commit -m "update"                    # Too vague
git commit -m "asdfghjkl"                 # Nonsense
git commit -m "Final final final commit"  # Unprofessional
git commit -m "Work in progress"          # Commit complete features
```

### Template
```
<Type>: <What you did>

<Type> = Add | Fix | Improve | Refactor | Docs | Test
<What> = 1 line, under 50 chars
```

---

## GitHub Useful Links

| Task | Link |
|------|------|
| Create SSH Key | https://github.com/settings/keys |
| View Your Repos | https://github.com/YOUR_USERNAME |
| Create New Repo | https://github.com/new |
| View Your Profile | https://github.com/settings/profile |
| Edit Repository Settings | https://github.com/USERNAME/REPO/settings |
| View Project | https://github.com/USERNAME/REPO |

---

## Keyboard Shortcuts & Tips

### Terminal Shortcuts
```
Ctrl + C        # Stop current command
Ctrl + L        # Clear screen
Tab             # Auto-complete file names
Up Arrow        # Previous command
```

### Useful Aliases (Optional)
Add to terminal config to shorten commands:
```bash
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push origin main'
alias gl='git log --oneline'
```

---

## Common Mistakes & Fixes

### "I committed something I shouldn't have!"
```bash
git revert HEAD                    # Undo last commit (creates new commit)
git push origin main
```

### "I added a huge file by accident"
```bash
git rm --cached huge_file.csv      # Remove from Git (keep locally)
echo "huge_file.csv" >> .gitignore # Add to .gitignore
git add .gitignore
git commit -m "Remove: huge data file, add to .gitignore"
git push origin main
```

### "I'm on wrong branch!"
```bash
git branch                         # See which branch you're on
git checkout main                  # Switch to main
git status
```

### "My changes conflict with GitHub's changes"
```bash
git pull origin main               # Get latest
# Fix conflicts in your editor
git add .
git commit -m "Merge: resolve conflicts"
git push origin main
```

---

## Projects Workflow (Step by Step)

### Starting a New Project
```bash
# 1. Create GitHub repo (github.com/new)
# 2. Clone to computer
git clone https://github.com/USERNAME/project-name.git
cd project-name

# 3. Make changes and commit
git add .
git commit -m "Initial: set up project structure"
git push origin main
```

### Adding Features
```bash
# Create feature branch (optional but recommended)
git checkout -b feature/add-model

# Make changes
git add .
git commit -m "Add: XGBoost model training"
git push origin feature/add-model

# On GitHub, open "Pull Request" to merge back to main
# (Or locally: git merge feature/add-model)
```

### Collaborating
```bash
git pull origin main               # Get latest from team
# Make your changes
git add .
git commit -m "Feature: ..."
git push origin main
```

---

## .gitignore Examples

Create `.gitignore` file in project root:

```
# Python
__pycache__/
*.pyc
venv/
.env

# Data (too large)
data/raw/
*.csv
*.xlsx

# Models (too large)
models/*.pkl
models/*.joblib

# IDE
.vscode/
.idea/
.DS_Store

# Results
results/*.png
results/*.json
```

Then commit it:
```bash
git add .gitignore
git commit -m "Add: .gitignore file"
```

---

## Your Minimal Daily Workflow

```bash
# Morning: Check status
git status

# During day: Make changes to files
# ... edit code ...

# Evening: Commit and push
git add .
git commit -m "What you accomplished"
git push origin main

# Next day: Pull latest (if working with others)
git pull origin main
```

---

## Resources

- **Interactive Practice:** https://learngitbranching.js.org
- **GitHub Docs:** https://docs.github.com
- **Cheat Sheet:** https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf
- **Pro Tip:** Google "[your error message] git" for solutions

---

## Remember

- ✅ Commit small, meaningful changes
- ✅ Write clear commit messages (future you will thank you)
- ✅ Push to GitHub regularly (backup!)
- ✅ Keep .gitignore updated (don't push 500MB CSV files!)
- ❌ Don't commit passwords or secret keys
- ❌ Don't panic if you mess up (Git has an undo for almost everything)

---

## Quick Test

Can you:
- [ ] Run `git status` and understand the output?
- [ ] Stage files with `git add .`?
- [ ] Commit with a clear message?
- [ ] Push to GitHub?
- [ ] See your changes on github.com?

If yes to all → **You're ready to deploy projects!** 🚀
