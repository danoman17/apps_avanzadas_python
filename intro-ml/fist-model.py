import pandas as pd

from sklearn.tree import DecisionTreeRegressor

# save filepath to variable for easier access
melbourne_file_path = './melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

#Selecting The Prediction Target
y = melbourne_data.Price

print(y)

#Choosing "Features"
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]
print(X)

print(X.describe())


# Building your model

#1 Define: What type of model will it be? A decision tree? Some other type of model? 
# Some other parameters of the model type are specified too.
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

#2 Fit model
melbourne_model.fit(X, y)

#making a prediction
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))