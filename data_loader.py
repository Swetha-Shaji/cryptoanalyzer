"""
Data Loading and Preprocessing Module
Handles loading, cleaning, and preparing Bitcoin data for analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_data(filepath):
    """
    Load Bitcoin OHLCV data from CSV file.
    
    Args:
        filepath (str): Path to the CSV file
    
    Returns:
        pd.DataFrame: Loaded dataframe with Date column parsed as datetime
    """
    df = pd.read_csv(filepath)
    
    # Use 'Start' column if 'Date' doesn't exist
    if 'Date' not in df.columns and 'Start' in df.columns:
        df['Date'] = df['Start']
        df = df.drop('Start', axis=1)
    
    # Parse Date column as datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort by date
    df = df.sort_values('Date').reset_index(drop=True)
    
    return df


def preprocess_data(df):
    """
    Preprocess the dataframe for Prophet model.
    Handles missing values and formats data in Prophet format (ds, y).
    
    Args:
        df (pd.DataFrame): Raw dataframe from load_data()
    
    Returns:
        pd.DataFrame: Preprocessed dataframe with 'ds' (Date) and 'y' (Close price)
    """
    # Create a copy to avoid modifying original
    df_processed = df.copy()
    
    # Check for missing values
    print(f"Missing values before handling:\n{df_processed.isnull().sum()}\n")
    
    # Forward fill for missing values in Close column (if any)
    df_processed['Close'] = df_processed['Close'].fillna(method='ffill').fillna(method='bfill')
    
    # Select only Date and Close columns, rename for Prophet format
    df_prophet = df_processed[['Date', 'Close']].copy()
    df_prophet.columns = ['ds', 'y']
    
    print(f"Data shape after preprocessing: {df_prophet.shape}")
    print(f"Date range: {df_prophet['ds'].min()} to {df_prophet['ds'].max()}\n")
    
    return df_prophet


def get_train_test_split(df_prophet, test_days=90):
    """
    Split data into train and test sets.
    Last test_days are used for testing.
    
    Args:
        df_prophet (pd.DataFrame): Preprocessed dataframe in Prophet format
        test_days (int): Number of days to reserve for testing
    
    Returns:
        tuple: (train_df, test_df)
    """
    split_point = len(df_prophet) - test_days
    train_df = df_prophet.iloc[:split_point].copy()
    test_df = df_prophet.iloc[split_point:].copy()
    
    print(f"Train set: {len(train_df)} samples ({train_df['ds'].min()} to {train_df['ds'].max()})")
    print(f"Test set: {len(test_df)} samples ({test_df['ds'].min()} to {test_df['ds'].max()})\n")
    
    return train_df, test_df
