import pandas as pd
reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print("---------------------------")

print(reviews.groupby('points').points.count())

print("---------------------------")

print(reviews.groupby('points').points.min())

print("---------------------------")

print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

print("---------------------------")

print(reviews.groupby(['country','province']).apply(lambda df: df.loc[df.points.idxmax()]))

print("---------------------------")

print(reviews.groupby(['country']).price.agg([len, min, max]))

print("---------------------------")

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)

print("---------------------------")

mi = countries_reviewed.index
print(type(mi))

print("---------------------------")

print(countries_reviewed.reset_index())

print("----------Sorting-----------------")

countries_reviewed = countries_reviewed.reset_index()

print(countries_reviewed.sort_values(by='len'))

print("---------------------------")

print(countries_reviewed.sort_values(by='len', ascending=False))

print(countries_reviewed.sort_index())

print("---------------------------")
print(countries_reviewed.sort_values(by=['country', 'len']))