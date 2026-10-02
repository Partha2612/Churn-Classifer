"""
Inference Module
Load trained model and make predictions on new customer data
"""

import pickle
import pandas as pd
import numpy as np
from preprocessing import create_preprocessing_pipeline


class ChurnPredictor:
    """Make predictions using trained churn model."""
    
    def __init__(self, model_path, preprocessor_path=None):
        """
        Initialize predictor with trained model.
        
        Args:
            model_path (str): Path to saved model file
            preprocessor_path (str): Path to saved preprocessor (optional)
        """
        # Load model
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        print(f"✅ Model loaded from {model_path}")
        
        # Load preprocessor if provided
        if preprocessor_path:
            with open(preprocessor_path, 'rb') as f:
                self.preprocessor = pickle.load(f)
            print(f"✅ Preprocessor loaded from {preprocessor_path}")
        else:
            self.preprocessor = None
    
    def predict(self, X):
        """
        Make predictions on new data.
        
        Args:
            X (np.ndarray or pd.DataFrame): Features for prediction
            
        Returns:
            dict: Dictionary with predictions and probabilities
        """
        # Preprocess if preprocessor available
        if self.preprocessor:
            X_processed = self.preprocessor.transform(X)
        else:
            X_processed = X
        
        # Get predictions
        predictions = self.model.predict(X_processed)
        probabilities = self.model.predict_proba(X_processed)[:, 1]
        
        return {
            'predictions': predictions,
            'probabilities': probabilities,
            'churn_risk': ['High' if p > 0.6 else 'Medium' if p > 0.4 else 'Low' 
                          for p in probabilities]
        }
    
    def predict_dataframe(self, df):
        """
        Make predictions and return results as DataFrame.
        
        Args:
            df (pd.DataFrame): Customer data with features
            
        Returns:
            pd.DataFrame: Original data + predictions
        """
        predictions = self.predict(df)
        
        result_df = df.copy()
        result_df['churn_prediction'] = predictions['predictions']
        result_df['churn_probability'] = predictions['probabilities']
        result_df['risk_level'] = predictions['churn_risk']
        
        return result_df


def main():
    """
    Example usage of ChurnPredictor.
    """
    print("\n" + "="*50)
    print("CUSTOMER CHURN PREDICTION - INFERENCE")
    print("="*50)
    
    # Load predictor
    predictor = ChurnPredictor('models/best_model.pkl')
    
    # Example: Load test data
    try:
        # Load original dataset
        df_all = pd.read_csv('data/Business_Analytics_Prediction_Classification_Dataset.csv')
        
        # Take first 10 customers as example
        df_new = df_all.head(10).copy()
        
        # Remove target column if present (for inference)
        if 'Churn' in df_new.columns:
            actual_churn = df_new['Churn'].copy()
            df_new = df_new.drop('Churn', axis=1)
        
        # Make predictions
        results = predictor.predict_dataframe(df_new)
        
        # Display results
        print("\n📊 PREDICTIONS ON SAMPLE DATA:")
        print("-"*50)
        
        display_cols = ['Customer_ID', 'Age', 'Annual_Spending', 
                       'Satisfaction_Score', 'churn_prediction', 
                       'churn_probability', 'risk_level']
        
        print(results[display_cols].to_string())
        
        # Show interpretation
        print("\n📋 PREDICTION INTERPRETATION:")
        print("-"*50)
        high_risk = (results['churn_probability'] > 0.6).sum()
        medium_risk = ((results['churn_probability'] > 0.4) & 
                      (results['churn_probability'] <= 0.6)).sum()
        low_risk = (results['churn_probability'] <= 0.4).sum()
        
        print(f"High Risk (>60%):   {high_risk} customers")
        print(f"Medium Risk (40-60%): {medium_risk} customers")
        print(f"Low Risk (<40%):    {low_risk} customers")
        
        # If actual labels available, show comparison
        if 'actual_churn' in locals():
            print("\n📈 ACCURACY CHECK (vs Actual):")
            print("-"*50)
            correct = (results['churn_prediction'] == (actual_churn == 'Yes').astype(int)).sum()
            accuracy = correct / len(results)
            print(f"Correct Predictions: {correct}/{len(results)} ({accuracy*100:.2f}%)")
        
    except FileNotFoundError:
        print("❌ Data file not found. Please ensure data exists at:")
        print("   data/Business_Analytics_Prediction_Classification_Dataset.csv")


if __name__ == "__main__":
    main()
