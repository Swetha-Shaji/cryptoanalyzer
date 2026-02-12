# 🚀 Quick Start Guide

Get your Bitcoin Price Forecasting application running in 5 minutes!

## What You'll Get

✅ Time series forecasting with Prophet ML
✅ Beautiful web dashboard with interactive forecasts
✅ Multiple forecast horizons (7, 30, 60, 90 days)
✅ Comprehensive model evaluation metrics
✅ Historical price analysis and visualizations

## Prerequisites

- Python 3.8+ installed
- CSV file with Bitcoin data ready
- ~10 minutes for first-time setup (Prophet installation takes time)

## Installation (5 Minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

**⏱️ Time**: 5-10 minutes (Prophet compilation)

### Step 2: Run the Application
```bash
python app.py
```

**⏱️ Time**: 2-5 minutes for first run (includes model training)

### Step 3: Open in Browser
```
http://localhost:5000
```

That's it! 🎉

## What Happens on First Run

1. **Data Loading** (10 sec)
   - Loads Bitcoin CSV file
   - Parses dates and sorts chronologically
   - Displays data summary

2. **Data Preprocessing** (5 sec)
   - Handles missing values
   - Formats for Prophet (ds, y columns)
   - Validates data quality

3. **Model Training** (30-90 sec)
   - Trains Prophet model on historical data
   - Detects trends and seasonality
   - Calibrates changepoint detection

4. **Model Evaluation** (10 sec)
   - Evaluates on test set (last 90 days)
   - Calculates MAE, RMSE, MAPE
   - Computes directional accuracy

5. **Visualization** (20 sec)
   - Generates historical price chart
   - Creates forecast plot
   - Creates evaluation comparison plot

6. **Web Server** (5 sec)
   - Starts Flask server
   - Ready for browser access

## Dashboard Overview

### Main Features

**📊 Key Statistics**
- Current Bitcoin price
- 30-day forecast price
- Predicted percentage change
- Model accuracy metrics

**🎛️ Forecast Selector**
Choose forecast horizon:
- 7 days ahead
- 30 days ahead
- 60 days ahead
- 90 days ahead

**📈 Visualizations**
- Historical price trends
- Forecast with uncertainty bands
- Actual vs predicted comparison

**📉 Model Metrics**
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute % Error)
- Directional Accuracy

## Common Operations

### Change Forecast Horizon
1. Click one of the horizon buttons (7, 30, 60, 90 days)
2. Dashboard automatically updates
3. New forecast appears instantly

### View Evaluation Metrics
All metrics are displayed on the main dashboard:
- **MAE**: Average prediction error in dollars
- **RMSE**: Error considering magnitude
- **MAPE**: Percentage-based accuracy
- **Directional Accuracy**: % correct up/down predictions

### Interpret the Forecast
- **Blue line**: Historical prices
- **Orange line**: Predicted future prices
- **Shaded area**: 95% confidence interval
- **Upper/Lower bounds**: Confidence range

## Troubleshooting Quick Fixes

### "Port 5000 already in use"
```bash
# Change port in app.py
app.run(port=5001)

# Or kill the process using port 5000
# (Instructions vary by OS - search "kill process on port 5000")
```

### "CSV file not found"
```bash
# Make sure file is in the project directory or data/ folder
# Check filename matches exactly
# Move file to: CryptoCurrency/bitcoin_2010-07-17_2024-05-23.csv
```

### "ModuleNotFoundError"
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Slow performance on first run
This is normal! Prophet takes time to train on large datasets.
Subsequent predictions are much faster.

## File Structure After Setup

```
CryptoCurrency/
├── app.py                          (Main Flask app)
├── train_model.py                  (Standalone training)
├── data_loader.py                  (Data handling)
├── prophet_model.py                (Model code)
├── model_evaluation.py             (Metrics)
├── eda.py                          (Visualizations)
├── bitcoin_2010-07-17_2024-05-23.csv  (Your data)
├── templates/index.html            (Dashboard HTML)
├── static/
│   ├── historical.png              (Generated plots)
│   ├── forecast.png
│   └── evaluation.png
└── model/
    └── prophet_model.pkl           (Saved model)
```

## Alternative: Run Training Only

To train the model without starting the web server:

```bash
python train_model.py
```

This generates all plots and metrics without the web interface.

## Advanced Options

### Use Different Port
Edit `app.py`, last line:
```python
app.run(port=5001)  # Use 5001 instead of 5000
```

### Disable Debug Mode (Production)
Edit `app.py`, last line:
```python
app.run(debug=False, host='0.0.0.0')
```

### Change Forecast Parameters
Edit `prophet_model.py`:
```python
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    changepoint_prior_scale=0.1  # Increase for more sensitivity
)
```

## Keyboard Shortcuts

While on the dashboard:
- **Refresh page**: `F5` (reload latest data)
- **Open DevTools**: `F12` (view network/console)

## Next Steps

1. ✅ Installation complete
2. ✅ Dashboard accessible
3. 📚 Read [README.md](README.md) for detailed documentation
4. ⚙️ Check [SETUP.md](SETUP.md) for advanced configuration
5. 📖 Explore [About page](http://localhost:5000/about) in dashboard

## Tips & Tricks

💡 **Bookmark the dashboard**
- Save http://localhost:5000 for quick access

💡 **Export plots**
- Right-click any plot and "Save image as"

💡 **Monitor the console**
- Console shows real-time predictions and errors
- Useful for debugging

💡 **Multiple browser tabs**
- Open multiple tabs to compare different horizons
- Side-by-side analysis

## Frequently Asked Questions

**Q: Why is the first run slow?**
A: Prophet needs to compile its C++ dependencies and train the model. Subsequent runs are much faster.

**Q: Can I change the data?**
A: Yes, replace the CSV file and restart the application.

**Q: Is this accurate for real trading?**
A: No! This is for educational purposes. Cryptocurrency is highly volatile.

**Q: Can I run this 24/7?**
A: Yes, but remember this is a development server. Use production WSGI for deployment.

**Q: What if I want to add more features?**
A: Check [README.md](README.md) for "Future Enhancements" ideas.

## Getting Help

1. Check console output for specific error messages
2. Review [SETUP.md](SETUP.md) for detailed troubleshooting
3. Read [README.md](README.md) for complete documentation
4. Check Prophet docs: https://facebook.github.io/prophet/

## Performance Expectations

| Operation | Time |
|-----------|------|
| First run (training) | 3-5 min |
| Subsequent runs | 30 sec |
| Page load | 2-3 sec |
| Forecast generation | <1 sec |
| Model training alone | 1-2 min |

---

**Ready to forecast Bitcoin prices? Start with `python app.py`!** 🚀📈

