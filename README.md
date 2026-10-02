# 🎯 Customer Churn Prediction Model

A machine learning project to predict customer churn using XGBoost with 73.35% ROC-AUC performance.

## 📊 Quick Results

| Metric | Score |
|--------|-------|
| **Accuracy** | 67.5% |
| **ROC-AUC** | 73.35% ⭐ |
| **Precision** | 61.86% |
| **Recall** | 68.87% |
| **F1 Score** | 65.18% |

## 🎯 Business Problem

**Goal:** Identify customers at risk of churning so the business can intervene with retention strategies.

**Why it matters:** 
- Precision of 62% means we minimize wasted retention efforts
- Recall of 69% means we catch ~7 out of 10 churners
- Helps prioritize high-value customer retention

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Model:** XGBoost (Gradient Boosting)
- **ML Libraries:** scikit-learn, pandas, numpy
- **Hyperparameter Tuning:** GridSearchCV (5-fold CV)
- **Evaluation:** Precision, Recall, F1, ROC-AUC, Confusion Matrix

## 📁 Project Structure

```
customer-churn-prediction/
├── README.md                    # This file
├── requirements.txt             # Package dependencies
├── .gitignore                   # Files to ignore in Git
│
├── data/
│   └── Business_Analytics_Prediction_Classification_Dataset.csv
│
├── notebooks/
│   └── churn_model_analysis.ipynb    # Full analysis & experiments
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py         # Data cleaning & feature engineering
│   ├── model.py                # Training & evaluation
│   └── inference.py            # Make predictions on new data
│
├── models/
│   └── best_model.pkl          # Trained XGBoost model (binary)
│
└── results/
    ├── model_performance.json   # Metrics summary
    ├── feature_importance.png   # Feature importance plot
    └── roc_curve.png           # ROC curve visualization
```

## 🚀 Quick Start
 
## USE 'Churn Notebook.ipynb'

            OR

    
### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model
```bash
python src/model.py
```
This will:
- Load & preprocess data
- Train XGBoost with GridSearchCV
- Save the best model
- Print performance metrics

### 4. Make Predictions
```bash
python src/inference.py
```

## 📈 Model Architecture

```
Raw Data (1200 samples, 20 features)
    ↓
[Preprocessing]
  - Handle missing values (SimpleImputer)
  - Encode categorical features (OneHotEncoder)
  - Remove ID columns
    ↓
[Feature Scaling]
  - StandardScaler for numerical features
    ↓
[XGBoost Classifier]
  - learning_rate: 0.05
  - max_depth: 1
  - n_estimators: 150
  - subsample: 0.8
    ↓
[Evaluation]
  - 5-fold cross-validation
  - ROC-AUC: 0.7335
```

## 🔍 Key Features & Their Impact

Top predictors of churn:
1. **Days Since Last Purchase** - Strongest indicator
2. **Satisfaction Score** - Lower satisfaction = higher churn risk
3. **Customer Tenure** - Newer customers churn more
4. **Complaints Last 12M** - More complaints = higher churn
5. **Discount %** - Discount-heavy customers tend to churn

## 💡 How to Use This for Predictions

```python
from src.preprocessing import load_and_prepare_data
from src.inference import predict_churn
import pandas as pd

# Load your new customer data
new_customers = pd.read_csv('new_customers.csv')

# Get predictions
predictions = predict_churn(new_customers)
# Returns: DataFrame with customer_id, churn_probability, predicted_class
```

## 📊 Model Performance Details

### Confusion Matrix
```
                Predicted
                No Churn  Churn
Actual No Churn   135      36
       Churn       44      85
```

**Interpretation:**
- TP (True Positives): 85 churners correctly identified
- FP (False Positives): 36 false alarms (retention effort wasted)
- FN (False Negatives): 44 missed churners (lost opportunity)
- TN (True Negatives): 135 correctly identified non-churners

### Why ROC-AUC is the key metric
ROC-AUC of 0.73 means the model is **73% better than random guessing** at distinguishing churners from non-churners. This is strong performance for this problem.

## 🔄 Model Development Process

1. **Exploratory Data Analysis (EDA)**
   - Analyzed 1200 customer records
   - 20 features across demographics, behavior, and spending
   - Identified class imbalance & missing values

2. **Feature Engineering**
   - Handled missing values with mean imputation
   - One-hot encoded categorical variables (Marketing_Channel, Membership_Type)
   - Applied StandardScaler to numerical features
   - Applied PCA for dimensionality reduction

3. **Model Comparison**
   - Logistic Regression (baseline)
   - Gradient Boosting Classifier
   - **XGBoost** (best performer) ⭐

4. **Hyperparameter Optimization**
   - GridSearchCV with 5-fold cross-validation
   - Tested 180 parameter combinations
   - Best params: `{'learning_rate': 0.05, 'max_depth': 1, 'n_estimators': 150, 'subsample': 0.8}`

## 📝 Next Steps / Future Improvements

- [ ] Implement SHAP values for feature interpretation
- [ ] Handle class imbalance with SMOTE
- [ ] Create Flask API for real-time predictions
- [ ] Deploy to AWS/Heroku
- [ ] Add probability calibration
- [ ] Collect more recent data for model refresh

## 👨‍💼 Author

**Partha Mukherjee**
- MBA in Business Analytics, St. Xavier's University
- Email: parthamukh26@gmail.com
- LinkedIn: [Your LinkedIn URL]
- Portfolio: [Your Portfolio URL]

## 📚 Files Reference

| File | Purpose |
|------|---------|
| `src/preprocessing.py` | Data loading, cleaning, feature engineering |
| `src/model.py` | Training pipeline, GridSearchCV, evaluation |
| `src/inference.py` | Load model, make predictions on new data |
| `notebooks/churn_model_analysis.ipynb` | Full analysis, visualizations, experiments |

## 📖 How to Learn from This Project

1. **Start with README** (you're here!)
2. **Read src/preprocessing.py** - Understand data pipeline
3. **Read src/model.py** - See training & evaluation
4. **Open Jupyter notebook** - See visualizations & full analysis
5. **Try inference.py** - Make predictions

## 🤝 Contributing

This is a portfolio project. If you have suggestions:
1. Fork the repository
2. Create a feature branch (`git checkout -b improvement/better-features`)
3. Commit changes (`git commit -m "Add SHAP interpretation"`)
4. Push to branch (`git push origin improvement/better-features`)
5. Open a Pull Request

## 📄 License

MIT License - feel free to use this project for learning and portfolio purposes.

---

**⭐ If you found this helpful, please star this repository!**

Last updated: September 2026
