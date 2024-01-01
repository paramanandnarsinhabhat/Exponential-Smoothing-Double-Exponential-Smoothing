# Double Exponential Smoothing for Time Series

This project applies Double Exponential Smoothing to time series data for forecasting, using the Holt-Winters method implemented through the `statsmodels` library.

## Installation

Ensure you have the following Python packages installed:
- pandas
- numpy
- matplotlib
- scikit-learn
- statsmodels

You can install them by running:
```
pip install -r requirements.txt
```

## Project Structure

```
EXPONENTIAL-SMOOTHING-DOUBLE-EXPONENTIAL-SMOOTHING/
│
├── data/
│   ├── train/
│   ├── valid/
├── myenv/
├── notebook/
│   └── Exponential smoothing models.ipynb
├── scripts/
│   └── time_series_double_exponential_smoothing.py
├── .gitignore
├── readme.md
└── requirements.txt
```

## Usage

The project includes a Jupyter notebook and a Python script for analysis:
- The notebook `Exponential smoothing models.ipynb` for interactive exploration.
- The script `time_series_double_exponential_smoothing.py` for running the analysis.

## Forecasting

The model is fitted with the training data and used to forecast the expected counts in the validation dataset. The forecasting performance is evaluated using the model's parameters and RMSE.
