# 🚀 Complete Step-by-Step: Push Your Churn Model to GitHub

## ✅ Prerequisites Checklist
- [ ] Git installed (test: `git --version`)
- [ ] GitHub account created (https://github.com/signup)
- [ ] SSH key generated and added to GitHub
- [ ] All project files downloaded locally
- [ ] Your churn prediction notebook & data file ready

---

## PHASE 1: Prepare Your Local Project (5 minutes)

### Step 1: Create Project Folder
Open terminal/command prompt and run:

```bash
# Create project directory
mkdir customer-churn-prediction
cd customer-churn-prediction
```

### Step 2: Copy Project Files
Place these files in your `customer-churn-prediction` folder:

```
customer-churn-prediction/
├── README.md                    (provided)
├── requirements.txt             (provided)
├── .gitignore                  (provided)
├── preprocessing.py            (provided)
├── model.py                    (provided)
├── inference.py                (provided)
├── GIT_GITHUB_GUIDE.md         (provided)
├── notebooks/
│   └── churn_model_analysis.ipynb    (your notebook)
└── data/
    └── Business_Analytics_Prediction_Classification_Dataset.csv
```

### Step 3: Create Folder Structure
```bash
mkdir -p notebooks data models results src
```

### Step 4: Move Files to Right Places
```bash
# Move your notebook
mv your_notebook.ipynb notebooks/churn_model_analysis.ipynb

# Move your data
mv Business_Analytics_Prediction_Classification_Dataset.csv data/

# Move Python modules to src
mkdir src
mv preprocessing.py model.py inference.py src/
```

Create `src/__init__.py` (empty file):
```bash
touch src/__init__.py
```

Update your imports in model.py and inference.py:
```python
# Change from:
from preprocessing import load_and_prepare_data

# To:
from src.preprocessing import load_and_prepare_data
```

### Step 5: Verify Folder Structure
```bash
# On Mac/Linux:
tree

# On Windows (PowerShell):
Get-ChildItem -Recurse
```

Should look like:
```
customer-churn-prediction/
├── README.md
├── requirements.txt
├── .gitignore
├── GIT_GITHUB_GUIDE.md
├── GITHUB_SETUP_STEPS.md
├── data/
│   └── Business_Analytics_Prediction_Classification_Dataset.csv
├── notebooks/
│   └── churn_model_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── model.py
│   └── inference.py
├── models/
│   └── (empty - will store trained model)
└── results/
    └── (empty - will store visualizations)
```

---

## PHASE 2: Initialize Git Locally (5 minutes)

### Step 6: Initialize Git Repository
```bash
cd customer-churn-prediction
git init
```

You'll see:
```
Initialized empty Git repository in /path/to/customer-churn-prediction/.git/
```

### Step 7: Configure Git (if not done before)
```bash
git config user.name "Your Full Name"
git config user.email "your.email@gmail.com"
```

### Step 8: Check Git Status
```bash
git status
```

Output should show all files in red (untracked):
```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        requirements.txt
        ...
```

### Step 9: Stage All Files
```bash
git add .
```

### Step 10: Check Staging Status
```bash
git status
```

Now files should be in green (staged):
```
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        ...
```

### Step 11: Make First Commit
```bash
git commit -m "Initial commit: Customer churn prediction model with XGBoost and 73% ROC-AUC"
```

Output:
```
[master (root-commit) a1b2c3d] Initial commit: Customer churn prediction model...
 15 files changed, 500 insertions(+)
```

---

## PHASE 3: Create GitHub Repository (3 minutes)

### Step 12: Go to GitHub and Create New Repo
1. Open https://github.com/new (or click "+" → "New repository")
2. Fill in:
   - **Repository name:** `customer-churn-prediction`
   - **Description:** "ML model to predict customer churn using XGBoost with 73.35% ROC-AUC"
   - **Visibility:** Public (so recruiters can see!)
   - **Initialize with:** Leave all UNCHECKED (we have our own files)
3. Click "Create repository"

### Step 13: Copy Your Repository URL
After creating, you'll see instructions. Copy the HTTPS or SSH URL:

**Example (SSH preferred):**
```
git@github.com:YOUR_USERNAME/customer-churn-prediction.git
```

**Example (HTTPS if SSH not working):**
```
https://github.com/YOUR_USERNAME/customer-churn-prediction.git
```

---

## PHASE 4: Push to GitHub (2 minutes)

### Step 14: Add Remote Repository
In your terminal (in the project folder):

```bash
git remote add origin git@github.com:YOUR_USERNAME/customer-churn-prediction.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Step 15: Verify Remote Connection
```bash
git remote -v
```

Should show:
```
origin  git@github.com:YOUR_USERNAME/customer-churn-prediction.git (fetch)
origin  git@github.com:YOUR_USERNAME/customer-churn-prediction.git (push)
```

### Step 16: Push Code to GitHub
```bash
git branch -M main
git push -u origin main
```

**First time might ask:** "Are you sure you want to continue connecting?"
Type: `yes` and press Enter

### Step 17: Verify on GitHub
1. Go to https://github.com/YOUR_USERNAME/customer-churn-prediction
2. You should see all your files there! 🎉

---

## PHASE 5: Optimize & Make it Recruiter-Ready (5 minutes)

### Step 18: Add a GitHub Profile Description

Edit your GitHub profile (https://github.com/settings/profile):
- Add profile picture
- Bio: "MBA in Business Analytics | ML Engineer | Finance & Data-Driven Problem Solver"

### Step 19: Pin This Repository
Go to https://github.com/YOUR_USERNAME and "Customize pinned repositories"
- Pin this project (and 2 others if you have them)

### Step 20: Add Topics to Your Repo
On your repo page → About section (gear icon) → Add topics:
```
machine-learning, customer-churn, xgboost, python, data-science, business-analytics
```

### Step 21: Add Badge to README (Optional but Cool)
Add this to the top of your README.md:

```markdown
[![GitHub](https://img.shields.io/badge/GitHub-customer--churn--prediction-blue?style=flat-square&logo=github)](https://github.com/YOUR_USERNAME/customer-churn-prediction)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-green?style=flat-square)](https://xgboost.readthedocs.io/)
[![ROC-AUC](https://img.shields.io/badge/ROC--AUC-73.35%25-success?style=flat-square)](https://github.com/YOUR_USERNAME/customer-churn-prediction)
```

---

## PHASE 6: Make Your First Update (to practice) (5 minutes)

### Step 22: Make a Small Change
Edit README.md and add your LinkedIn:
```markdown
## 👨‍💼 Author

**Partha Mukherjee**
- MBA in Business Analytics, St. Xavier's University
- Email: parthamukh26@gmail.com
- LinkedIn: [https://linkedin.com/in/YOUR_PROFILE](https://linkedin.com/in/YOUR_PROFILE)
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
```

### Step 23: Stage, Commit, Push
```bash
git add README.md
git commit -m "Docs: add author contact information"
git push origin main
```

### Step 24: Verify on GitHub
Refresh https://github.com/YOUR_USERNAME/customer-churn-prediction
You should see the update!

---

## FUTURE UPDATES: Standard Workflow

Every time you improve your model or add features:

```bash
# 1. Make your changes
# ... edit files ...

# 2. Check what changed
git status

# 3. Stage everything
git add .

# 4. Commit with descriptive message
git commit -m "Improve: add SHAP feature interpretation"

# 5. Push to GitHub
git push origin main
```

---

## Troubleshooting

### Problem: "fatal: 'origin' does not appear to be a 'git' repository"
**Solution:** Make sure you're in the project folder
```bash
cd customer-churn-prediction
```

### Problem: "Permission denied (publickey)"
**Solution:** SSH key not set up. Use HTTPS instead:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/customer-churn-prediction.git
git push -u origin main
```

### Problem: "Please tell me who you are"
**Solution:** Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"
```

### Problem: "Updates were rejected because the remote contains work that you do not have locally"
**Solution:** Pull latest changes first
```bash
git pull origin main
```

---

## What to Share with Recruiters

### LinkedIn Post Template:
```
🚀 Project: Customer Churn Prediction Model

Just completed a machine learning project to predict customer churn 
using XGBoost with 73.35% ROC-AUC performance.

Key highlights:
✅ 1200 customer records analyzed
✅ XGBoost + GridSearchCV hyperparameter tuning
✅ Comprehensive preprocessing pipeline
✅ Feature importance analysis
✅ Production-ready code structure

Check it out → [GitHub link]

#MachineLearning #DataScience #XGBoost #Python #Analytics
```

### Email to Recruiter:
```
Subject: Customer Churn Prediction - Machine Learning Portfolio Project

Hi [Recruiter Name],

I recently completed a customer churn prediction project that demonstrates 
my machine learning and data engineering skills.

Project Details:
- Trained XGBoost classifier on 1,200 customer records
- Achieved 73.35% ROC-AUC using GridSearchCV hyperparameter tuning
- Built production-ready Python modules for preprocessing, training, and inference
- Full documentation and clean code structure

GitHub Repository: https://github.com/YOUR_USERNAME/customer-churn-prediction

The project showcases:
✅ End-to-end ML pipeline design
✅ Feature engineering & preprocessing
✅ Model evaluation & interpretation
✅ Professional code documentation

I'd love to discuss this project and explore how similar approaches could 
solve challenges at [Company Name].

Best regards,
Partha
```

---

## Next Steps After Upload

1. ✅ Get the GitHub link
2. ✅ Add to your LinkedIn profile (Projects section)
3. ✅ Update your resume with GitHub link
4. ✅ Share in job applications
5. ✅ Continue improving the model (SHAP, better features, etc.)
6. ✅ Create 2-3 more projects to build portfolio

---

## You're All Set! 🎉

Your churn prediction model is now:
- ✅ Version controlled with Git
- ✅ Hosted on GitHub for the world to see
- ✅ Professional and recruiter-ready
- ✅ Ready to share in job applications

**Next time you want to update:**
```bash
cd customer-churn-prediction
# Make changes
git add .
git commit -m "Clear description of what you changed"
git push origin main
```

Good luck! Your GitHub portfolio will help you land data science roles! 🚀
