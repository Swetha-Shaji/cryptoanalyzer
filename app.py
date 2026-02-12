"""
Flask Web Application for Bitcoin Price Forecasting
Displays historical data, forecasts, and evaluation metrics
with interactive forecast horizon selection
"""

from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pathlib import Path
import io
import base64
from datetime import datetime

# Use Agg backend to avoid display issues in Flask
matplotlib.use('Agg')

from data_loader import load_data, preprocess_data, get_train_test_split
from prophet_model import train_prophet_model, generate_forecast, plot_forecast, save_model, load_model
from model_evaluation import evaluate_model, print_evaluation_metrics, plot_evaluation
from eda import plot_historical_price, plot_price_statistics, print_data_summary

# Initialize Flask app
app = Flask(__name__)

# Get project root directory
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / 'data'
STATIC_DIR = PROJECT_ROOT / 'static'
MODEL_DIR = PROJECT_ROOT / 'model'

# Ensure directories exist
STATIC_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

# Global variables to store model and data
model = None
df_original = None
train_df = None
test_df = None
metrics = None
forecast_cache = {}


def initialize_app():
    """
    Initialize the application by loading data and training the model.
    This function runs once at startup.
    """
    global model, df_original, train_df, test_df, metrics
    
    print("\n" + "=" * 60)
    print("INITIALIZING CRYPTOCURRENCY FORECASTING APPLICATION")
    print("=" * 60 + "\n")
    
    # Find CSV file in data directory
    csv_files = list(DATA_DIR.glob('*.csv')) if DATA_DIR.exists() else []
    
    if not csv_files:
        # Check in root directory
        csv_files = list(PROJECT_ROOT.glob('*.csv'))
    
    if not csv_files:
        print("ERROR: No CSV file found!")
        print(f"Looked in: {DATA_DIR} and {PROJECT_ROOT}")
        return False
    
    csv_path = csv_files[0]
    print(f"Loading data from: {csv_path}\n")
    
    try:
        # Step 1: Load and preprocess data
        df_original = load_data(str(csv_path))
        print_data_summary(df_original)
        
        df_prophet = preprocess_data(df_original)
        
        # Step 2: Create train/test split
        train_df, test_df = get_train_test_split(df_prophet, test_days=90)
        
        # Step 3: Train Prophet model
        model = train_prophet_model(train_df)
        
        # Step 4: Evaluate model
        metrics = evaluate_model(model, test_df)
        print_evaluation_metrics(metrics)
        
        # Step 5: Generate and save plots
        print("Generating visualizations...\n")
        
        # Historical price plot
        hist_path = STATIC_DIR / 'historical.png'
        plot_historical_price(df_original, save_path=str(hist_path))
        
        # Forecast plot (30 days default)
        forecast = generate_forecast(model, periods=30)
        forecast_path = STATIC_DIR / 'forecast.png'
        plot_forecast(model, forecast, save_path=str(forecast_path))
        
        # Evaluation plot
        eval_path = STATIC_DIR / 'evaluation.png'
        plot_evaluation(metrics['combined'], save_path=str(eval_path))
        
        # Save model
        model_path = MODEL_DIR / 'prophet_model.pkl'
        save_model(model, str(model_path))
        
        print("\n" + "=" * 60)
        print("INITIALIZATION COMPLETE - APPLICATION READY")
        print("=" * 60 + "\n")
        
        return True
        
    except Exception as e:
        print(f"ERROR during initialization: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


@app.route('/')
def index():
    """
    Home page route displaying historical data, forecast, and metrics.
    Includes form to select forecast horizon.
    """
    if model is None or df_original is None:
        return "Error: Application not properly initialized. Check the console logs.", 500
    
    # Get forecast horizon from request (default: 30 days)
    horizon = request.args.get('horizon', 30, type=int)
    
    # Validate horizon
    if horizon not in [7, 30, 60, 90]:
        horizon = 30
    
    # Generate forecast for selected horizon
    forecast = generate_forecast(model, periods=horizon)
    
    # Get last actual price and first forecast price
    last_actual_price = df_original['Close'].iloc[-1]
    forecast_price_in_30 = forecast.iloc[-1]['yhat']
    forecast_price_low = forecast.iloc[-1]['yhat_lower']
    forecast_price_high = forecast.iloc[-1]['yhat_upper']
    
    # Calculate percentage change
    pct_change = ((forecast_price_in_30 - last_actual_price) / last_actual_price) * 100
    
    return render_template(
        'index.html',
        metrics=metrics,
        horizon=horizon,
        last_actual_price=f"${last_actual_price:,.2f}",
        forecast_price=f"${forecast_price_in_30:,.2f}",
        forecast_price_low=f"${forecast_price_low:,.2f}",
        forecast_price_high=f"${forecast_price_high:,.2f}",
        pct_change=f"{pct_change:+.2f}%",
        last_date=df_original['Date'].iloc[-1].strftime('%Y-%m-%d'),
        forecast_date=(df_original['Date'].iloc[-1] + pd.Timedelta(days=horizon)).strftime('%Y-%m-%d')
    )


@app.route('/api/forecast', methods=['GET'])
def api_forecast():
    """
    API endpoint to get forecast data for a specific horizon.
    Returns JSON with forecast details.
    """
    if model is None:
        return jsonify({'error': 'Model not initialized'}), 500
    
    horizon = request.args.get('horizon', 30, type=int)
    
    # Generate forecast
    forecast = generate_forecast(model, periods=horizon)
    
    # Prepare response
    forecast_data = {
        'dates': forecast.tail(horizon)['ds'].dt.strftime('%Y-%m-%d').tolist(),
        'predictions': forecast.tail(horizon)['yhat'].round(2).tolist(),
        'upper_bound': forecast.tail(horizon)['yhat_upper'].round(2).tolist(),
        'lower_bound': forecast.tail(horizon)['yhat_lower'].round(2).tolist(),
    }
    
    return jsonify(forecast_data)


@app.route('/api/metrics', methods=['GET'])
def api_metrics():
    """
    API endpoint to get model evaluation metrics.
    """
    if metrics is None:
        return jsonify({'error': 'Metrics not computed'}), 500
    
    metrics_data = {
        'mae': round(metrics['mae'], 2),
        'rmse': round(metrics['rmse'], 2),
        'mape': round(metrics['mape'], 2),
        'directional_accuracy': round(metrics['directional_accuracy'], 2)
    }
    
    return jsonify(metrics_data)


@app.route('/about')
def about():
    """
    About page with information about the model and data.
    """
    return render_template('about.html')


if __name__ == '__main__':
    # Initialize the application
    success = initialize_app()
    
    if success:
        # Run Flask app
        print("Starting Flask server on http://localhost:5000\n")
        app.run(debug=True, host='localhost', port=5000)
    else:
        print("Failed to initialize application. Please check the errors above.")
