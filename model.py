"""
Model Training & Evaluation Module
Trains XGBoost classifier with GridSearchCV and evaluates performance
"""

import pickle
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, roc_curve, classification_report
)
from xgboost import XGBClassifier
from preprocessing import load_and_prepare_data


class ChurnModelTrainer:
    """Train and evaluate customer churn prediction model."""
    
    def __init__(self, random_state=42):
        """
        Initialize trainer.
        
        Args:
            random_state (int): Random seed for reproducibility
        """
        self.random_state = random_state
        self.model = None
        self.best_params = None
        self.metrics = {}
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.y_test_pred = None
        self.y_test_prob = None
    
    def split_data(self, X, y, test_size=0.2):
        """
        Split data into train and test sets.
        
        Args:
            X (np.ndarray): Features
            y (np.ndarray): Target
            test_size (float): Proportion for test set
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state, stratify=y
        )
        
        print(f"\nData split:")
        print(f"  Train: {self.X_train.shape[0]} samples")
        print(f"  Test:  {self.X_test.shape[0]} samples")
    
    def train_with_grid_search(self):
        """
        Train XGBoost with GridSearchCV for hyperparameter optimization.
        """
        print("\n" + "="*50)
        print("HYPERPARAMETER TUNING (GridSearchCV)")
        print("="*50)
        
        xgb_model = XGBClassifier(random_state=self.random_state, n_jobs=-1)
        
        param_grid = {
            'learning_rate': [0.01, 0.05, 0.1],
            'max_depth': [1, 2, 3],
            'n_estimators': [50, 100, 150, 200],
            'subsample': [0.7, 0.8, 1.0],
            'min_samples_leaf': [2, 5, 10],
            'min_samples_split': [5, 10, 20]
        }
        
        grid = GridSearchCV(
            estimator=xgb_model,
            param_grid=param_grid,
            cv=5,
            scoring='accuracy',
            n_jobs=-1,
            verbose=1
        )
        
        print("\nFitting GridSearchCV (this may take 2-5 minutes)...")
        grid.fit(self.X_train, self.y_train)
        
        self.model = grid.best_estimator_
        self.best_params = grid.best_params_
        
        print(f"\n✅ Best Parameters Found:")
        for param, value in self.best_params.items():
            print(f"   {param}: {value}")
        print(f"\n✅ Best Cross-Validation Accuracy: {grid.best_score_:.4f}")
    
    def evaluate(self):
        """
        Evaluate model on test set.
        """
        if self.model is None:
            raise ValueError("Model not trained yet. Call train_with_grid_search() first.")
        
        print("\n" + "="*50)
        print("MODEL EVALUATION (Test Set)")
        print("="*50)
        
        # Predictions
        self.y_test_pred = self.model.predict(self.X_test)
        self.y_test_prob = self.model.predict_proba(self.X_test)[:, 1]
        
        # Calculate metrics
        self.metrics = {
            'accuracy': accuracy_score(self.y_test, self.y_test_pred),
            'precision': precision_score(self.y_test, self.y_test_pred),
            'recall': recall_score(self.y_test, self.y_test_pred),
            'f1_score': f1_score(self.y_test, self.y_test_pred),
            'roc_auc': roc_auc_score(self.y_test, self.y_test_prob)
        }
        
        # Print results
        print("\n📊 TEST SET METRICS:")
        print(f"  Accuracy:  {self.metrics['accuracy']:.4f} ({self.metrics['accuracy']*100:.2f}%)")
        print(f"  Precision: {self.metrics['precision']:.4f} ({self.metrics['precision']*100:.2f}%)")
        print(f"  Recall:    {self.metrics['recall']:.4f} ({self.metrics['recall']*100:.2f}%)")
        print(f"  F1 Score:  {self.metrics['f1_score']:.4f}")
        print(f"  ROC-AUC:   {self.metrics['roc_auc']:.4f} ⭐")
        
        # Classification report
        print("\n📋 DETAILED CLASSIFICATION REPORT:")
        print(classification_report(self.y_test, self.y_test_pred, 
                                   target_names=['No Churn', 'Churn']))
    
    def plot_confusion_matrix(self, save_path=None):
        """
        Plot confusion matrix.
        
        Args:
            save_path (str): Path to save figure
        """
        cm = confusion_matrix(self.y_test, self.y_test_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True,
                   xticklabels=['No Churn', 'Churn'],
                   yticklabels=['No Churn', 'Churn'])
        plt.title('Confusion Matrix - Churn Prediction Model')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"\n✅ Confusion matrix saved to {save_path}")
        plt.close()
    
    def plot_roc_curve(self, save_path=None):
        """
        Plot ROC curve.
        
        Args:
            save_path (str): Path to save figure
        """
        fpr, tpr, _ = roc_curve(self.y_test, self.y_test_prob)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='darkblue', lw=2, 
                label=f'ROC Curve (AUC = {self.metrics["roc_auc"]:.3f})')
        plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--', label='Random Classifier')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve - XGBoost Churn Model')
        plt.legend(loc="lower right")
        plt.grid(alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✅ ROC curve saved to {save_path}")
        plt.close()
    
    def plot_feature_importance(self, feature_names, save_path=None, top_n=15):
        """
        Plot feature importance from XGBoost.
        
        Args:
            feature_names (list): Names of features
            save_path (str): Path to save figure
            top_n (int): Number of top features to show
        """
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[-top_n:]
        
        plt.figure(figsize=(10, 8))
        plt.barh(range(len(indices)), importances[indices], color='steelblue')
        plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
        plt.xlabel('Importance Score')
        plt.title(f'Top {top_n} Feature Importance - XGBoost Model')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✅ Feature importance plot saved to {save_path}")
        plt.close()
    
    def save_model(self, filepath):
        """
        Save trained model to disk.
        
        Args:
            filepath (str): Path to save model
        """
        with open(filepath, 'wb') as f:
            pickle.dump(self.model, f)
        print(f"✅ Model saved to {filepath}")
    
    def save_metrics(self, filepath):
        """
        Save metrics to JSON file.
        
        Args:
            filepath (str): Path to save metrics
        """
        metrics_dict = {
            'accuracy': float(self.metrics['accuracy']),
            'precision': float(self.metrics['precision']),
            'recall': float(self.metrics['recall']),
            'f1_score': float(self.metrics['f1_score']),
            'roc_auc': float(self.metrics['roc_auc']),
            'best_params': self.best_params
        }
        
        with open(filepath, 'w') as f:
            json.dump(metrics_dict, f, indent=2)
        print(f"✅ Metrics saved to {filepath}")


def main():
    """
    Main training pipeline.
    """
    print("\n" + "="*50)
    print("CUSTOMER CHURN PREDICTION MODEL")
    print("="*50)
    
    # Load and prepare data
    print("\n📂 LOADING DATA")
    print("-"*50)
    data = load_and_prepare_data('data/Business_Analytics_Prediction_Classification_Dataset.csv')
    
    # Initialize trainer
    trainer = ChurnModelTrainer()
    
    # Split data
    print("\n✂️ SPLITTING DATA")
    print("-"*50)
    trainer.split_data(data['X_processed'], data['y'])
    
    # Train with hyperparameter tuning
    trainer.train_with_grid_search()
    
    # Evaluate
    trainer.evaluate()
    
    # Create visualizations
    print("\n📊 GENERATING VISUALIZATIONS")
    print("-"*50)
    trainer.plot_confusion_matrix('results/confusion_matrix.png')
    trainer.plot_roc_curve('results/roc_curve.png')
    trainer.plot_feature_importance(data['feature_names'], 'results/feature_importance.png')
    
    # Save model and metrics
    print("\n💾 SAVING MODEL & RESULTS")
    print("-"*50)
    trainer.save_model('models/best_model.pkl')
    trainer.save_metrics('results/model_performance.json')
    
    print("\n" + "="*50)
    print("✅ TRAINING COMPLETE!")
    print("="*50)


if __name__ == "__main__":
    main()
