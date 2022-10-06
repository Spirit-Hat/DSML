import pandas as pd
import os

dir_path = "dataset"
res = []

for path in os.listdir(dir_path):
    res.append(path)
print(res)
# df = pd.read_csv("dataset/nyt1.csv")

data = pd.read_excel("dataset/rollingsales_manhattan.xls", skiprows=4)
data.columns = [column.lower().replace("\n", "").replace(" ", "_").replace("-", "_") for column in data.columns]
# data = data[data.year_built > 0]

data_price_zero = data[data.saleprice <=10].borough.count()
print(data_price_zero)
print(data.columns)
print(data.saleprice)