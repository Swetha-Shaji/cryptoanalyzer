"""
Standalone Training Script
Run this script to train the model and generate all plots without running the Flask server.
Usage: python train_model.py
"""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent

# Import all modules
from data_loader import load_data, preprocess_data, get_train_test_split
from prophet_model import (
    train_prophet_model, 
    generate_forecast, 
    plot_forecast, 
    plot_components,
    save_model
)
from model_evaluation import evaluate_model, print_evaluation_metrics, plot_evaluation
from eda import plot_historical_price, plot_price_statistics, print_data_summary


def main():
    """
    Main training function - runs the complete pipeline
    """
    print("\n" + "=" * 70)
    print("BITCOIN PRICE FORECASTING - MODEL TRAINING SCRIPT")
    print("=" * 70 + "\n")
    
    # Directories
    data_dir = PROJECT_ROOT / 'data'
    static_dir = PROJECT_ROOT / 'static'
    model_dir = PROJECT_ROOT / 'model'
    
    # Create directories if they don't exist
    static_dir.mkdir(exist_ok=True)
    model_dir.mkdir(exist_ok=True)
    
    # Step 1: Find and load CSV file
    print("Step 1: Loading Data")
    print("-" * 70)
    
    csv_files = list(data_dir.glob('*.csv')) if data_dir.exists() else []
    
    if not csv_files:
        csv_files = list(PROJECT_ROOT.glob('*.csv'))
    
    if not csv_files:
        print("❌ ERROR: No CSV file found!")
        print(f"   Please place a CSV file in {data_dir} or {PROJECT_ROOT}")
        return False
    
    csv_path = csv_files[0]
    print(f"✓ Found CSV file: {csv_path.name}\n")
    
    try:
        # Load data
        df_original = load_data(str(csv_path))
        print("✓ Data loaded successfully\n")
        
        # Step 2: Data Summary
        print("Step 2: Data Summary")
        print("-" * 70)
        print_data_summary(df_original)
        
        # Step 3: Data Preprocessing
        print("Step 3: Data Preprocessing")
        print("-" * 70)
        df_prophet = preprocess_data(df_original)
        print("✓ Data preprocessed for Prophet\n")
        
        # Step 4: Train/Test Split
        print("Step 4: Creating Train/Test Split")
        print("-" * 70)
        train_df, test_df = get_train_test_split(df_prophet, test_days=90)
        print("✓ Data split completed\n")
        
        # Step 5: Train Prophet Model
        print("Step 5: Training Prophet Model")
        print("-" * 70)
        model = train_prophet_model(train_df)
        print("✓ Model training completed\n")
        
        # Step 6: Model Evaluation
        print("Step 6: Model Evaluation")
        print("-" * 70)
        metrics = evaluate_model(model, test_df)
        print_evaluation_metrics(metrics)
        
        # Step 7: Generate Forecasts
        print("Step 7: Generating Forecasts")
        print("-" * 70)
        forecast_30 = generate_forecast(model, periods=30)
        print("✓ 30-day forecast generated")
        forecast_90 = generate_forecast(model, periods=90)
        print("✓ 90-day forecast generated\n")
        
        # Step 8: Create Visualizations
        print("Step 8: Creating Visualizations")
        print("-" * 70)
        
        # Historical price plot
        hist_path = static_dir / 'historical.png'
        plot_historical_price(df_original, save_path=str(hist_path))
        
        # Price statistics plot
        stats_path = static_dir / 'statistics.png'
        plot_price_statistics(df_original, save_path=str(stats_path))
        
        # Forecast plot
        forecast_path = static_dir / 'forecast.png'
        plot_forecast(model, forecast_30, title="Bitcoin 30-Day Price Forecast", 
                      save_path=str(forecast_path))
        
        # Components plot
        components_path = static_dir / 'components.png'
        plot_components(model, forecast_90, save_path=str(components_path))
        
        # Evaluation plot
        eval_path = static_dir / 'evaluation.png'
        plot_evaluation(metrics['combined'], save_path=str(eval_path))
        
        print("✓ All visualizations saved\n")
        
        # Step 9: Save Model
        print("Step 9: Saving Model")
        print("-" * 70)
        model_path = model_dir / 'prophet_model.pkl'
        save_model(model, str(model_path))
        print()
        
        # Summary
        print("=" * 70)
        print("TRAINING COMPLETED SUCCESSFULLY")
        print("=" * 70)
        print(f"\n📊 Generated Files:")
        print(f"   - {hist_path.relative_to(PROJECT_ROOT)}")
        print(f"   - {stats_path.relative_to(PROJECT_ROOT)}")
        print(f"   - {forecast_path.relative_to(PROJECT_ROOT)}")
        print(f"   - {components_path.relative_to(PROJECT_ROOT)}")
        print(f"   - {eval_path.relative_to(PROJECT_ROOT)}")
        print(f"   - {model_path.relative_to(PROJECT_ROOT)}")
        
        print(f"\n📈 Key Results:")
        print(f"   - MAE: ${metrics['mae']:.2f}")
        print(f"   - RMSE: ${metrics['rmse']:.2f}")
        print(f"   - MAPE: {metrics['mape']:.2f}%")
        print(f"   - Directional Accuracy: {metrics['directional_accuracy']:.2f}%")
        
        # Forecast summary
        last_price = df_original['Close'].iloc[-1]
        forecast_30_price = forecast_30.iloc[-1]['yhat']
        pct_change = ((forecast_30_price - last_price) / last_price) * 100
        
        print(f"\n🔮 Forecast (30 days):")
        print(f"   - Current Price: ${last_price:,.2f}")
        print(f"   - Forecasted Price: ${forecast_30_price:,.2f}")
        print(f"   - Expected Change: {pct_change:+.2f}%")
        print(f"   - Upper Bound: ${forecast_30.iloc[-1]['yhat_upper']:,.2f}")
        print(f"   - Lower Bound: ${forecast_30.iloc[-1]['yhat_lower']:,.2f}")
        
        print(f"\n💡 Next Steps:")
        print(f"   1. Run 'python app.py' to start the Flask web server")
        print(f"   2. Open http://localhost:5000 in your browser")
        print(f"   3. Interact with the dashboard to explore forecasts")
        
        print("\n" + "=" * 70 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR during training: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
