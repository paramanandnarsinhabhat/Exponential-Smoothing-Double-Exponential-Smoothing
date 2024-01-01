import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


from sklearn.metrics import mean_squared_error
from math import sqrt
from statistics import mean 
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings
warnings.filterwarnings("ignore")

train_data = pd.read_csv("/Users/paramanandbhat/Downloads/5_-_exponential_smoothing_models (2)/data/train_data.csv")
valid_data = pd.read_csv("/Users/paramanandbhat/Downloads/5_-_exponential_smoothing_models (2)/data/valid_data.csv")

#Required Preprocessing
train_data.timestamp = pd.to_datetime(train_data['Date'],format='%Y-%m-%d')
train_data.index = train_data.timestamp

valid_data.timestamp = pd.to_datetime(valid_data['Date'],format='%Y-%m-%d')
valid_data.index = valid_data.timestamp

model = ExponentialSmoothing(np.asarray(train_data['count']), trend='add')
model_fit = model.fit(smoothing_level=0.7, smoothing_slope=0.0001)

valid_data['Holt_linear'] = model_fit.forecast(len(valid_data))

print(model_fit.params)


print(model.params)