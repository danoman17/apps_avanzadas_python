import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 5)


reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)

print("---------------------------")
print(reviews.points.describe())
print("---------------------------")


print(reviews.taster_name.describe())
print("---------------------------")

print(reviews.points.mean())
print("---------------------------")


print(reviews.taster_name.unique())
print("---------------------------")

print(reviews.taster_name.value_counts())


#maps
print("-----------maps-----------")

# review_points_mean = reviews.points.mean()
# reviews.points.map(lambda p: p - review_points_mean)

# print(reviews['points'])

review_points_mean = reviews.points.mean()

print(reviews.points - review_points_mean)
print("---------------------------")


print(reviews.country + " - " + reviews.region_1)


