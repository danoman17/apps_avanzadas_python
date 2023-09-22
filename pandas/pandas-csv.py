import pandas as pd

# Ejemplo de como leer archivos csv
datos = pd.read_csv("./data.csv");
print(datos) #imprime nan por las comas, para solucionarlo solo quita las comas en el .csv


# Ejemplo del tutorial de kaggle
wine_reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0);

print(wine_reviews.shape)
print(wine_reviews.head())