import pandas as pd
import os


def district(borough: int):
    if borough == 1:
        return "Manhattan"
    elif borough == 2:
        return "Bronx"
    elif borough == 3:
        return "Brooklyn"
    elif borough == 4:
        return "Queens"
    elif borough == 5:
        return "Staten"


if __name__ == '__main__':

    dir_path = "dataset/"
    res = []
    data = []
    for path in os.listdir(dir_path):
        res.append(path)
        dirty_data = pd.read_excel(dir_path + path, skiprows=4)
        dirty_data.columns = [column.lower().replace("\n", "")
                              .replace(" ", "_").replace("-", "_")
                              for column in
                              dirty_data.columns]
        data.append(dirty_data)
    # df = pd.read_csv("dataset/nyt1.csv")
    data = pd.concat(data)

    data.insert(1, "district", [district(a) for a in data.borough])
    print(data.columns)
    print(data)

    # data = data[data.year_built > 0]

    data_price_zero = data[data.saleprice <= 10].borough.count()
    print(data_price_zero)
    print(data.columns)
    print(data.saleprice)
