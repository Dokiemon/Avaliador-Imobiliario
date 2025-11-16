import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train():
    csv_path = "houses_to_rent.csv"
    data = pd.read_csv(csv_path)

    #tratamento dos dados
    for i in range(len(data)):
        if data.loc[i, "floor"] == "-":
            data.loc[i, "floor"] = 0
        if data.loc[i, "animal"] == "acept":
            data.loc[i, "animal"] = 1
        elif data.loc[i, "animal"] == "not acept":
            data.loc[i, "animal"] = 0
        if data.loc[i, "furniture"] == "furnished":
            data.loc[i, "furniture"] = 1
        elif data.loc[i, "furniture"] == "not furnished":
            data.loc[i, "furniture"] = 0
        if data.loc[i, "total"]:
            if "R$" in data.loc[i, "total"]:
                data.loc[i, "total"] = data.loc[i, "total"].replace("R$", "")
                data.loc[i, "total"] = data.loc[i, "total"].replace(",", "")

    data["floor"] = data["floor"].astype(int)
    data["animal"] = data["animal"].astype(int)
    data["furniture"] = data["furniture"].astype(int)
    data["total"] = data["total"].astype(float)
    data = data.drop(columns = ["city", "hoa", "rent amount", "property tax", "fire insurance"])
    print("-------------------")
    print(data.dtypes)
    X = data.drop(columns = "total") #o X aramzena todas as colunas do dataframe exceto (drop) a coluna alvo (MedHouseVal)
    y = data["total"]

    model = LinearRegression() #criou o objeto
    model.fit(X, y) #treinou o objeto

    return model