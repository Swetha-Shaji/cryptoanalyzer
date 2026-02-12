#  cryptoanalyzer

##  Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Data

Ensure your Bitcoin CSV file is in the project directory. Required columns:

- `Date` - Trading date
- `Open` - Opening price
- `High` - Highest price
- `Low` - Lowest price
- `Close` - Closing price
- `Volume` - Trading volume

### 3. Run the Application

```bash
python app.py
```

The application will:
1. Load and preprocess the data
2. Train the Prophet model
3. Generate evaluation metrics
4. Create visualization plots
5. Start the Flask server

### 4. Access the Web Interface

Open your browser and navigate to:

```
http://localhost:5000
```

---

##  Features

### Dashboard
-  Historical price visualization
-  Future price forecasts with confidence intervals
-  Model performance metrics (MAE, RMSE, MAPE)
-  Actual vs Predicted price comparison
-  Interactive forecast horizon selection (7, 30, 60, 90 days)

### Data Processing
- Automatic datetime parsing
- Missing value handling
- Data validation and cleaning
- Train/test split for evaluation

### Prophet Model
- Automatic trend detection
- Yearly and weekly seasonality
- Changepoint detection
- Uncertainty quantification
- 95% confidence intervals

### Evaluation Metrics
- **MAE**: Mean Absolute Error - Average prediction error
- **RMSE**: Root Mean Squared Error - Penalizes large errors
- **MAPE**: Mean Absolute Percentage Error - Percentage-based accuracy
- **Directional Accuracy**: Percentage of correct up/down predictions

---
