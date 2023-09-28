import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)



print("--------Renaming---------------------")

print(reviews.rename(columns={'points':'score'}))

print("-----------------------------")

print(reviews.rename(index={0:'firstEntry', 1:'secondEntry'}))

print("-----------------------------")

print(reviews.rename_axis("wines", axis='rows').rename_axis("fields",axis='columns'))
