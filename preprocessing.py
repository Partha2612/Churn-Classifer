"""
Data Preprocessing Module
Handles data loading, cleaning, and feature engineering for churn prediction
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load customer data from CSV file.
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"Data shape: {df.shape}")
    return df


def explore_data(df: pd.DataFrame) -> None:
    """
    Print basic data information for EDA.
    
    Args:
        df (pd.DataFrame): Input dataset
    """
    print("\n=== DATA OVERVIEW ===")
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nTarget Variable Distribution:\n{df['Churn'].value_counts()}")
    print(f"Churn Rate: {df['Churn'].value_counts(normalize=True)}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean data by:
    - Removing ID columns
    - Converting target variable to binary
    - Handling data types
    
    Args:
        df (pd.DataFrame): Raw dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset
    """
    df_clean = df.copy()
    
    # Remove ID column (not useful for model)
    if 'Customer_ID' in df_clean.columns:
        df_clean = df_clean.drop('Customer_ID', axis=1)
    
    # Convert Churn to binary (Yes -> 1, No -> 0)
    if 'Churn' in df_clean.columns:
        df_clean['Churn'] = (df_clean['Churn'] == 'Yes').astype(int)
    
    print(f"\nCleaned data shape: {df_clean.shape}")
    return df_clean


def separate_features_target(df: pd.DataFrame) -> tuple:
    """
    Separate features (X) from target (y).
    
    Args:
        df (pd.DataFrame): Cleaned dataset
        
    Returns:
        tuple: (X, y) where X is features and y is target
    """
    y = df['Churn']
    X = df.drop('Churn', axis=1)
    
    print(f"\nFeatures shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    
    return X, y


def identify_feature_types(X: pd.DataFrame) -> tuple:
    """
    Identify numerical and categorical columns.
    
    Args:
        X (pd.DataFrame): Feature matrix
        
    Returns:
        tuple: (numerical_cols, categorical_cols)
    """
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    
    print(f"\nNumerical columns ({len(numerical_cols)}): {numerical_cols}")
    print(f"Categorical columns ({len(categorical_cols)}): {categorical_cols}")
    
    return numerical_cols, categorical_cols


def create_preprocessing_pipeline(numerical_cols: list, categorical_cols: list):
    """
    Create scikit-learn preprocessing pipeline.
    
    Args:
        numerical_cols (list): List of numerical column names
        categorical_cols (list): List of categorical column names
        
    Returns:
        ColumnTransformer: Preprocessing pipeline
    """
    # Pipeline for numerical features
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    # Pipeline for categorical features
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    # Combine both pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )
    
    return preprocessor


def preprocess_data(X: pd.DataFrame, preprocessor, fit=True):
    """
    Apply preprocessing pipeline to features.
    
    Args:
        X (pd.DataFrame): Features to preprocess
        preprocessor: Fitted or unfitted preprocessing pipeline
        fit (bool): Whether to fit the preprocessor
        
    Returns:
        np.ndarray: Preprocessed features
    """
    if fit:
        X_processed = preprocessor.fit_transform(X)
        print("\nPreprocessor fitted on training data")
    else:
        X_processed = preprocessor.transform(X)
        print("\nPreprocessor applied to new data")
    
    print(f"Processed data shape: {X_processed.shape}")
    
    return X_processed


def load_and_prepare_data(filepath: str) -> dict:
    """
    End-to-end data loading and preparation.
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        dict: Dictionary with prepared data and preprocessing pipeline
    """
    # Load and explore
    df = load_data(filepath)
    explore_data(df)
    
    # Clean
    df_clean = clean_data(df)
    
    # Separate features and target
    X, y = separate_features_target(df_clean)
    
    # Identify feature types
    numerical_cols, categorical_cols = identify_feature_types(X)
    
    # Create preprocessing pipeline
    preprocessor = create_preprocessing_pipeline(numerical_cols, categorical_cols)
    
    # Apply preprocessing
    X_processed = preprocess_data(X, preprocessor, fit=True)
    
    return {
        'X_processed': X_processed,
        'y': y.values,
        'preprocessor': preprocessor,
        'numerical_cols': numerical_cols,
        'categorical_cols': categorical_cols,
        'feature_names': X.columns.tolist()
    }


# Example usage
if __name__ == "__main__":
    # This runs if you execute this file directly
    try:
        data_dict = load_and_prepare_data('data/Business_Analytics_Prediction_Classification_Dataset.csv')
        print("\n✅ Data preprocessing completed successfully!")
    except FileNotFoundError:
        print("❌ Data file not found. Please check the filepath.")
