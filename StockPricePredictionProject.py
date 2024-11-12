import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
import os
from datetime import datetime

import warnings


warnings.filterwarnings("ignore")
data = pd.read_csv('all_stocks_5yr.csv', delimiter=',', on_bad_lines='skip') 
print(data.shape)
print(data.sample(7))