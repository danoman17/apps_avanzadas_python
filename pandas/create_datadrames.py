import pandas as pd

df = pd.DataFrame({'Yes': [50, 21, 10, 9], 'No': [131, 2, 5, 6]})

print(df)

dfs = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(dfs)

dfp = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
print(dfp)


serie1 = pd.Series([1, 2, 3, 4, 5])

print(serie1)

serie2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

print(serie2)

