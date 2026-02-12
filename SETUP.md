# Installation & Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Windows, macOS, or Linux

## Step-by-Step Installation

### 1. Install Python Dependencies

Open PowerShell or Command Prompt and run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Pandas (data manipulation)
- NumPy (numerical computing)
- Prophet (time series forecasting)
- Matplotlib (visualization)
- Scikit-learn (machine learning metrics)

**Note**: Prophet installation may take a few minutes as it includes dependencies.

### 2. Verify Data File

Ensure your CSV file is in one of these locations:
- `c:\Users\haris\OneDrive\Desktop\CryptoCurrency\bitcoin_2010-07-17_2024-05-23.csv`
- Or in the `data/` subdirectory

The file must contain these columns:
```
Date, Open, High, Low, Close, Volume
```

### 3. Directory Structure

After setup, your project should look like:

```
CryptoCurrency/
├── app.py
├── train_model.py
├── data_loader.py
├── prophet_model.py
├── model_evaluation.py
├── eda.py
├── requirements.txt
├── README.md
├── bitcoin_2010-07-17_2024-05-23.csv
├── data/
├── templates/
│   ├── index.html
│   └── about.html
├── static/
│   ├── historical.png
│   ├── forecast.png
│   └── evaluation.png
└── model/
    └── prophet_model.pkl
```

## Running the Application

### Option 1: Full Training + Web Server

```bash
python app.py
```

This will:
1. Load the Bitcoin data
2. Train the Prophet model
3. Generate evaluation metrics
4. Create visualization plots
5. Start Flask server on http://localhost:5000

**Time**: First run takes 2-5 minutes (includes model training)

### Option 2: Training Only (No Web Server)

```bash
python train_model.py
```

This will:
1. Train the model
2. Generate all plots
3. Save the trained model
4. Print evaluation metrics
5. Exit without starting the web server

### Option 3: Using Jupyter Notebook

Create a new Jupyter notebook and run:

```python
from data_loader import load_data, preprocess_data
from prophet_model import train_prophet_model, generate_forecast
import matplotlib.pyplot as plt

# Load data
df = load_data('bitcoin_2010-07-17_2024-05-23.csv')
df_prophet = preprocess_data(df)

# Train model
model = train_prophet_model(df_prophet)

# Generate forecast
forecast = generate_forecast(model, periods=30)

# Plot
fig = model.plot(forecast)
plt.show()
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'prophet'"

**Solution**: Reinstall Prophet with specific version
```bash
pip install --upgrade prophet==1.1.4
```

### Issue: "FileNotFoundError: [Errno 2] No such file or directory: '...csv'"

**Solution**: 
1. Check the CSV file exists in the project directory
2. Verify the filename matches exactly
3. Try moving CSV to the `data/` subdirectory

### Issue: "Port 5000 already in use"

**Solution**: Either:
1. Stop the other process using port 5000
2. Change port in app.py: `app.run(port=5001)`

### Issue: Long installation time for Prophet

**Note**: Prophet compilation takes time (5-15 minutes on first install).
This is normal. Be patient and let it complete.

### Issue: "cmdstanpy" compilation errors

**Solution** (if you encounter cmdstanpy issues):
```bash
pip install --no-cache-dir pystan==2.19.1.1
pip install --no-cache-dir cmdstanpy==1.1.0
pip install --no-cache-dir prophet==1.1.4
```

### Issue: Matplotlib backend errors

**Solution**: The app uses 'Agg' backend which doesn't require display.
If you see warnings, they can be safely ignored.

## Configuration Options

### Modify Model Parameters

Edit `prophet_model.py` to adjust Prophet settings:

```python
# Increase changepoint sensitivity (more trend changes detected)
model = Prophet(changepoint_prior_scale=0.1)

# Adjust seasonality strength
model = Prophet(seasonality_prior_scale=20)

# Disable yearly seasonality
model = Prophet(yearly_seasonality=False)
```

### Change Flask Settings

Edit `app.py`:

```python
# Change port
app.run(port=5001)

# Disable debug mode for production
app.run(debug=False)

# Allow external connections
app.run(host='0.0.0.0')
```

### Adjust Train/Test Split

Edit `data_loader.py`:

```python
# Use last 120 days for testing instead of 90
train_df, test_df = get_train_test_split(df_prophet, test_days=120)
```

## Performance Notes

### Typical Execution Times

- **First Run** (with model training): 3-5 minutes
- **Web Server Start**: 30 seconds
- **Page Load**: 2-3 seconds
- **Forecast Generation**: <1 second

### Memory Usage

- **RAM Required**: ~500 MB
- **Disk Space**: ~100 MB (including plots)
- **Model Size**: ~2-3 MB

### Large Dataset Considerations

If using data with >10,000 days:
1. Prophet training may take longer
2. Consider splitting into smaller periods
3. Increase timeout if using cloud platforms

## Security Considerations

⚠️ **Important**: This is a development application.

For production deployment:
1. Set `debug=False` in Flask
2. Use a production WSGI server (Gunicorn, etc.)
3. Add input validation
4. Use HTTPS/SSL certificate
5. Implement rate limiting
6. Add authentication if needed

```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Updating Dependencies

To update all packages to their latest versions:

```bash
pip install --upgrade -r requirements.txt
```

To check for outdated packages:

```bash
pip list --outdated
```

## Uninstalling

To remove all project dependencies:

```bash
pip uninstall -r requirements.txt -y
```

## Getting Help

If you encounter issues:

1. Check the console output for error messages
2. Verify all files are in correct locations
3. Ensure CSV file has correct format
4. Check Python version: `python --version`
5. Review the README.md for more details

## Next Steps

After successful installation:

1. Run `python app.py`
2. Open http://localhost:5000
3. Explore the dashboard
4. Try different forecast horizons
5. Review model evaluation metrics
6. Check the About page for more information

## Additional Resources

- [Prophet Documentation](https://facebook.github.io/prophet/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Time Series Forecasting](https://otexts.com/fpp2/)

---

**Happy Forecasting! 🚀📊**
