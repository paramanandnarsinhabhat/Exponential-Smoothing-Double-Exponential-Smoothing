import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


from sklearn.metrics import mean_squared_error
from math import sqrt
from statistics import mean 

import warnings
warnings.filterwarnings("ignore")

train_data = pd.read_csv("/Users/paramanandbhat/Downloads/5_-_exponential_smoothing_models (2)/data/train_data.csv")
valid_data = pd.read_csv("/Users/paramanandbhat/Downloads/5_-_exponential_smoothing_models (2)/data/valid_data.csv")
