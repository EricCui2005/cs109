import pandas as pd
from scipy.special import expit
import numpy as np

# Loading data
data = pd.read_csv('simple/simple-train.csv')

# Excluding the label
params = [0] * (data.shape[1] - 1)

# Hyperparameters
learn = 0.0001
steps = 1000

# Steps
for _ in range(steps):
    
    # Initializing gradients
    gradient = [0] * (data.shape[1] - 1) 

    # Iterating through rows
    for row_tuple in data.iterrows():
        
        # Extracting features and labels
        row = list(row_tuple[1])
        features = row[:-1]
        label = row[-1]

        # Iterating through features
        for i in range(len(features)):
            gradient[i] += features[i] * (label - expit((np.dot(params, features))))
       
    # Multiplying gradient values by learn rate 
    gradient = [learn * val for val in gradient]

    for i in range(len(params)):
        params[i] += gradient[i]
    
print(params)