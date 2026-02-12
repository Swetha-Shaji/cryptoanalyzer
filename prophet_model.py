"""
Prophet Model Training and Forecasting Module
Handles Prophet model initialization, training, and generating forecasts
"""

import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
from pathlib import Path
import pickle


def train_prophet_model(train_df, yearly_seasonality=True, weekly_seasonality=True):
    """
    Initialize and train Prophet model on historical data.
    
    Args:
        train_df (pd.DataFrame): Training data with 'ds' (date) and 'y' (price) columns
        yearly_seasonality (bool): Whether to include yearly seasonality
        weekly_seasonality (bool): Whether to include weekly seasonality
    
    Returns:
        Prophet: Trained Prophet model
    """
    # Initialize Prophet model with custom seasonality settings
    model = Prophet(
        yearly_seasonality=yearly_seasonality,
        weekly_seasonality=weekly_seasonality,
        daily_seasonality=False,
        interval_width=0.95,
        changepoint_prior_scale=0.05
    )
    
    print("Training Prophet model...")
    # Fit model on training data
    model.fit(train_df)
    print("Model training completed.\n")
    
    return model


def create_future_dataframe(model, periods):
    """
    Create a future dataframe for making predictions.
    
    Args:
        model (Prophet): Trained Prophet model
        periods (int): Number of days to forecast
    
    Returns:
        pd.DataFrame: Future dataframe with 'ds' column
    """
    future = model.make_future_dataframe(periods=periods)
    return future


def generate_forecast(model, periods):
    """
    Generate forecast for specified number of days.
    
    Args:
        model (Prophet): Trained Prophet model
        periods (int): Number of days to forecast
    
    Returns:
        pd.DataFrame: Forecast dataframe with predictions and uncertainty intervals
    """
    future = create_future_dataframe(model, periods)
    forecast = model.predict(future)
    
    return forecast


def plot_forecast(model, forecast, title="Bitcoin Price Forecast", save_path=None):
    """
    Plot forecast using Prophet's built-in plotting.
    
    Args:
        model (Prophet): Trained Prophet model
        forecast (pd.DataFrame): Forecast dataframe
        title (str): Title for the plot
        save_path (str): Path to save the plot image
    
    Returns:
        matplotlib.figure.Figure: Matplotlib figure object
    """
    fig = model.plot(forecast)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=100, bbox_inches='tight')
        print(f"Forecast plot saved to {save_path}")
    
    return fig


def plot_components(model, forecast, save_path=None):
    """
    Plot Prophet model components (trend, seasonality, etc).
    
    Args:
        model (Prophet): Trained Prophet model
        forecast (pd.DataFrame): Forecast dataframe
        save_path (str): Path to save the plot image
    
    Returns:
        matplotlib.figure.Figure: Matplotlib figure object
    """
    fig = model.plot_components(forecast)
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=100, bbox_inches='tight')
        print(f"Components plot saved to {save_path}")
    
    return fig


def save_model(model, filepath):
    """
    Save trained Prophet model to pickle file.
    
    Args:
        model (Prophet): Trained Prophet model
        filepath (str): Path to save the model
    """
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {filepath}")


def load_model(filepath):
    """
    Load previously saved Prophet model.
    
    Args:
        filepath (str): Path to the saved model
    
    Returns:
        Prophet: Loaded Prophet model
    """
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    print(f"Model loaded from {filepath}")
    return model
