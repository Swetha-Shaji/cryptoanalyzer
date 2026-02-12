#!/usr/bin/env python3
"""
Bitcoin Price Forecasting Application - Startup Guide

This is a summary of how to get the application running.
"""

# ============================================================================
#                        QUICK START GUIDE
# ============================================================================

"""
INSTALLATION (First Time Only)
==============================

Step 1: Open PowerShell or Command Prompt
Step 2: Navigate to the project directory
Step 3: Run this command:

    pip install -r requirements.txt

This will install all necessary Python libraries.
Installation time: 5-15 minutes (first time due to Prophet compilation)


RUNNING THE APPLICATION
=======================

Option 1: Full Application with Web Server
-------------------------------------------
Command:
    python app.py

This will:
- Load Bitcoin data
- Train the Prophet model (2-5 minutes for first run)
- Generate all plots and metrics
- Start Flask web server
- Listen on http://localhost:5000

Then open your browser and go to:
    http://localhost:5000


Option 2: Training Only (No Web Server)
----------------------------------------
Command:
    python train_model.py

This will:
- Load Bitcoin data
- Train the model
- Generate all plots
- Print metrics to console
- Exit (no web server)

Useful for: Testing model without opening browser


EXPECTED FIRST RUN OUTPUT
==========================

When you run 'python app.py', you'll see:

    ============================================================
    INITIALIZING CRYPTOCURRENCY FORECASTING APPLICATION
    ============================================================

    Loading data from: bitcoin_2010-07-17_2024-05-23.csv

    ============================================================
    DATA SUMMARY
    ============================================================
    Date range: 2010-07-17 to 2024-05-23
    Total trading days: 5109
    Close Price Statistics:
      Min: $0.05
      Max: $73,750.00
      Mean: $15,423.45
      ...

    Data shape after preprocessing: (5109, 2)
    ...

    Training Prophet model...
    Model training completed.

    Train set: 5020 samples
    Test set: 90 samples

    ==================================================
    MODEL EVALUATION METRICS (TEST SET)
    ==================================================
    Mean Absolute Error (MAE):     $1,234.56
    Root Mean Squared Error (RMSE): $1,567.89
    Mean Absolute Percentage Error (MAPE): 3.45%
    Directional Accuracy:          65.43%
    ==================================================

    Generating visualizations...
    Historical plot saved to static/historical.png
    Forecast plot saved to static/forecast.png
    Evaluation plot saved to static/evaluation.png
    Model saved to model/prophet_model.pkl

    ============================================================
    INITIALIZATION COMPLETE - APPLICATION READY
    ============================================================

    Starting Flask server on http://localhost:5000


Then you can:
1. Open browser to http://localhost:5000
2. See the dashboard
3. Click forecast horizon buttons (7, 30, 60, 90 days)
4. View predictions and metrics


WHEN YOU'RE DONE
================

In the console/terminal, press: Ctrl+C

This will:
- Stop the Flask server
- Close the application
- Return to command prompt


FILE STRUCTURE CREATED
======================

After successful run, you'll have:

CryptoCurrency/
├── Python Files (ready to use):
│   ├── app.py
│   ├── data_loader.py
│   ├── prophet_model.py
│   ├── model_evaluation.py
│   ├── eda.py
│   └── train_model.py
│
├── Web Templates (created):
│   └── templates/
│       ├── index.html
│       └── about.html
│
├── Generated Plots:
│   └── static/
│       ├── historical.png
│       ├── forecast.png
│       ├── evaluation.png
│       ├── statistics.png
│       └── components.png
│
├── Generated Model:
│   └── model/
│       └── prophet_model.pkl
│
├── Configuration:
│   ├── requirements.txt
│   └── bitcoin_2010-07-17_2024-05-23.csv
│
└── Documentation:
    ├── README.md
    ├── QUICKSTART.md
    ├── SETUP.md
    ├── PROJECT_GUIDE.md
    ├── ARCHITECTURE.md
    ├── COMPLETION_SUMMARY.md
    └── FILE_INDEX.md


TROUBLESHOOTING
===============

Problem: "CSV file not found"
Solution: 
- Check bitcoin_2010-07-17_2024-05-23.csv is in project root
- Or place it in the data/ subfolder
- Check filename matches exactly (case-sensitive)

Problem: "ModuleNotFoundError: No module named 'prophet'"
Solution:
- Run: pip install --upgrade prophet==1.1.4
- Or: pip install -r requirements.txt --no-cache-dir

Problem: "Port 5000 already in use"
Solution:
- Edit app.py, change port 5000 to 5001 (last line)
- Or stop the other process using port 5000

Problem: Installation takes forever
Solution:
- This is normal! Prophet compilation takes 5-15 minutes
- Keep the terminal open and wait
- Don't interrupt the process

Problem: "Connection refused" when opening localhost:5000
Solution:
- Wait for "Flask server on http://localhost:5000" message
- Make sure you're using the exact URL: http://localhost:5000
- Check that Python console shows no errors


NEXT STEPS
==========

1. ✅ Run: pip install -r requirements.txt
2. ✅ Run: python app.py
3. ✅ Open: http://localhost:5000 in your browser
4. ✅ Click the horizon buttons (7, 30, 60, 90 days)
5. ✅ Review the forecasts and metrics
6. ✅ Check the About page for more info
7. ✅ Read README.md for detailed documentation


DOCUMENTATION
==============

Quick References:
- QUICKSTART.md - 5-minute setup (read first!)
- README.md - Complete guide
- SETUP.md - Installation details
- PROJECT_GUIDE.md - Deep dive
- ARCHITECTURE.md - System design

Code Files:
- app.py - Main Flask application
- data_loader.py - Data loading
- prophet_model.py - Model training
- model_evaluation.py - Metrics
- eda.py - Visualization


KEYBOARD SHORTCUTS
==================

While running the app:

Ctrl+C            - Stop the Flask server
F5                - Refresh the dashboard page
Click buttons     - Change forecast horizon
Click About       - See documentation page


TYPICAL SESSION
===============

1. Open PowerShell/Command Prompt (5 sec)
2. Navigate to CryptoCurrency folder (5 sec)
3. Run: pip install -r requirements.txt (5-10 minutes)
4. Run: python app.py (2-5 minutes on first run)
5. Open browser to http://localhost:5000 (2 sec)
6. Explore dashboard (5-10 minutes)
7. Press Ctrl+C to stop server (2 sec)

Total time: 12-25 minutes (first time)
Subsequent runs: 30-60 seconds


UNDERSTANDING THE DASHBOARD
============================

Top Section:
- Shows current Bitcoin price
- Shows 30-day forecast price
- Shows expected percentage change
- Shows model accuracy metrics

Buttons:
- Click 7 Days to forecast 7 days ahead
- Click 30 Days to forecast 30 days ahead
- Click 60 Days to forecast 60 days ahead
- Click 90 Days to forecast 90 days ahead

Metrics Cards:
- MAE: Average prediction error in dollars
- RMSE: Error considering magnitude
- MAPE: Percentage-based accuracy
- Accuracy: % of correct up/down predictions

Plots:
1. Historical Price - Shows all past prices
2. Forecast - Shows predicted future prices with range
3. Evaluation - Shows how model performed on test data


WHAT'S HAPPENING UNDER THE HOOD
================================

When you run 'python app.py':

1. Python starts Flask web framework
2. Loads bitcoin_2010-07-17_2024-05-23.csv
3. Cleans data and handles missing values
4. Splits into training (5020 days) and testing (90 days)
5. Trains Prophet model on training data
6. Evaluates on test data
7. Calculates MAE, RMSE, MAPE, Accuracy
8. Generates 3-4 plot images
9. Saves trained model to pickle file
10. Stores all in memory for web requests
11. Starts web server on localhost:5000
12. Waits for browser requests

When you visit http://localhost:5000:

1. Browser requests the home page
2. Flask app.py receives request
3. Renders index.html template
4. Fills in data (prices, metrics, plots)
5. Sends HTML to browser
6. Browser displays the dashboard

When you click a horizon button:

1. Browser requests with new horizon parameter
2. Flask regenerates forecast for new horizon
3. Calculates new metrics
4. Sends updated page
5. Browser displays new forecast


CUSTOMIZATION (Advanced)
=========================

To change forecast port:
- Edit app.py, last line
- Change: app.run(port=5000)
- To: app.run(port=5001)

To change Prophet parameters:
- Edit prophet_model.py
- Modify the Prophet() initialization

To change dashboard appearance:
- Edit templates/index.html
- Modify CSS styles and HTML elements

To change model evaluation period:
- Edit data_loader.py
- Change test_days parameter


IMPORTANT NOTES
===============

⚠️  This is for EDUCATIONAL purposes only!
⚠️  Do NOT use this for real financial decisions!
⚠️  Cryptocurrency is highly volatile and unpredictable!
⚠️  Past performance does NOT guarantee future results!
⚠️  Always consult with financial professionals!

✅ Use this to LEARN about time series forecasting
✅ Use this to understand Prophet model
✅ Use this to practice Python and Flask
✅ Use this to explore cryptocurrency data


PERFORMANCE EXPECTATIONS
=========================

First Run:
- Model training: 2-5 minutes
- Plot generation: 30-60 seconds
- Dashboard load: 5-10 seconds
- Total: 3-7 minutes

Subsequent Runs:
- Application start: 30 seconds
- Forecast generation: <1 second
- Dashboard load: 2-3 seconds

Memory Usage:
- Running application: ~200-300 MB
- Trained model: ~5-10 MB

Disk Usage:
- Plots: ~5 MB
- Model pickle: ~3-5 MB


GETTING HELP
============

If something goes wrong:

1. Check console/terminal for error messages
2. Read SETUP.md for troubleshooting
3. Check QUICKSTART.md for common issues
4. Review PROJECT_GUIDE.md for details
5. Check code comments in Python files
6. Look at About page in dashboard


FREQUENTLY ASKED QUESTIONS
==========================

Q: Why does first run take so long?
A: Prophet compiles C++ code. This is normal.

Q: Can I use this to trade crypto?
A: NO! It's educational only. Don't use for real trading.

Q: What if CSV is not found?
A: Place it in project root or data/ folder.

Q: Can I change the port?
A: Yes, edit app.py last line: app.run(port=YOUR_PORT)

Q: How often should I retrain?
A: You can retrain whenever new data is available.

Q: Can I forecast more than 90 days?
A: Yes, edit app.py to add more button options.

Q: Is this accurate?
A: It's a reasonable forecast, but crypto is unpredictable.

Q: Can I deploy to cloud?
A: Yes, see SETUP.md for deployment options.

Q: Can I use different data?
A: Yes, replace CSV with your own Bitcoin data.


SUMMARY
=======

You now have a complete Bitcoin forecasting application!

Quick steps:
1. pip install -r requirements.txt
2. python app.py
3. Open http://localhost:5000
4. Click buttons to explore forecasts
5. Press Ctrl+C to stop

Documentation:
- Start with QUICKSTART.md
- Then read README.md
- Then explore PROJECT_GUIDE.md

Have fun exploring time series forecasting! 🚀📊
"""

# ============================================================================

if __name__ == '__main__':
    print(__doc__)
    print("\nTo run the application, use one of these commands:\n")
    print("1. For full application: python app.py")
    print("2. For training only: python train_model.py")
    print("\nThen visit: http://localhost:5000")
