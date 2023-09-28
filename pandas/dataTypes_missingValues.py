
import pandas as pd
reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
print("--------Dtypes---------------------")

print(reviews.price.dtype)

print("-----------------------------")

print(reviews.dtypes)

print("-----------------------------")

print(reviews.points.astype('float64'))

print("-----------------------------")

print(reviews.index.dtype)

print("-----------------------------")

print(reviews[pd.isnull(reviews.country)])


print("-----------------------------")

print(reviews.region_2.fillna("Unknown"))

print("-----------------------------")

print(reviews.taster_twitter_handle.replace("@kerinokeefe","@kerino"))