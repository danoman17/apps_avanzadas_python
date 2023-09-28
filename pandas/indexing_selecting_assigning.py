import pandas as pd

# Ejemplo del tutorial de kaggle
reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0);

print(reviews['country'])

print(reviews.iloc[0])

print(reviews.iloc[:, 0])

print(reviews.iloc[:3, 0])


