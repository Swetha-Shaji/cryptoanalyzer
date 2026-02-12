"""
Model Evaluation Module
Handles train/test split evaluation and metrics calculation (MAE, RMSE)
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt


def evaluate_model(model, test_df):
    """
    Evaluate model on test set and calculate MAE and RMSE.
    
    Args:
        model (Prophet): Trained Prophet model
        test_df (pd.DataFrame): Test dataframe with 'ds' and 'y' columns
    
    Returns:
        dict: Dictionary containing evaluation metrics and predictions
    """
    # Create future dataframe for test period
    future = model.make_future_dataframe(periods=len(test_df))
    forecast = model.predict(future)
    
    # Get predictions for test period
    test_forecast = forecast.tail(len(test_df))[['ds', 'yhat']].reset_index(drop=True)
    test_actual = test_df.reset_index(drop=True)
    
    # Align dataframes
    combined = pd.DataFrame({
        'ds': test_actual['ds'],
        'actual': test_actual['y'],
        'predicted': test_forecast['yhat']
    })
    
    # Calculate metrics
    mae = mean_absolute_error(combined['actual'], combined['predicted'])
    rmse = np.sqrt(mean_squared_error(combined['actual'], combined['predicted']))
    mape = np.mean(np.abs((combined['actual'] - combined['predicted']) / combined['actual'])) * 100
    
    # Calculate directional accuracy (correct up/down prediction)
    actual_direction = np.diff(combined['actual']) > 0
    predicted_direction = np.diff(combined['predicted']) > 0
    directional_accuracy = np.mean(actual_direction == predicted_direction) * 100
    
    metrics = {
        'mae': mae,
        'rmse': rmse,
        'mape': mape,
        'directional_accuracy': directional_accuracy,
        'test_forecast': test_forecast,
        'combined': combined
    }
    
    return metrics


def print_evaluation_metrics(metrics):
    """
    Print evaluation metrics in a formatted way.
    
    Args:
        metrics (dict): Dictionary containing evaluation metrics
    """
    print("=" * 50)
    print("MODEL EVALUATION METRICS (TEST SET)")
    print("=" * 50)
    print(f"Mean Absolute Error (MAE):     ${metrics['mae']:.2f}")
    print(f"Root Mean Squared Error (RMSE): ${metrics['rmse']:.2f}")
    print(f"Mean Absolute Percentage Error (MAPE): {metrics['mape']:.2f}%")
    print(f"Directional Accuracy:          {metrics['directional_accuracy']:.2f}%")
    print("=" * 50)
    print()


def plot_evaluation(combined, save_path=None):
    """
    Plot actual vs predicted prices on test set.
    
    Args:
        combined (pd.DataFrame): Combined actual and predicted dataframe
        save_path (str): Path to save the plot image
    
    Returns:
        matplotlib.figure.Figure: Matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    ax.plot(combined['ds'], combined['actual'], label='Actual Price', 
            linewidth=2, marker='o', markersize=4, color='#1f77b4')
    ax.plot(combined['ds'], combined['predicted'], label='Predicted Price', 
            linewidth=2, marker='s', markersize=4, color='#ff7f0e', linestyle='--')
    
    ax.set_title('Bitcoin Price: Actual vs Predicted (Test Set)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price (USD)', fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=100, bbox_inches='tight')
        print(f"Evaluation plot saved to {save_path}")
    
    return fig
