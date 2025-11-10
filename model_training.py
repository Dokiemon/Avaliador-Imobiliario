import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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

data["floor"] = data["floor"].astype(int)
data["animal"] = data["animal"].astype(int)
data["furniture"] = data["furniture"].astype(int)
print("-------------------")
print(data.dtypes)
# X = data_transformed.drop(columns = "total") #o X aramzena todas as colunas do dataframe exceto (drop) a coluna alvo (MedHouseVal)
# y = data_transformed["total"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# model = LinearRegression() #criou o objeto
# model.fit(X_train, y_train) #treinou o objeto

# y_pred = model.predict(X_test)

# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print("Taxa Erro Médio Absoluto: ", mae)
# print("Taxa Erro Médio Quadrático: ", mse)
# print("Coeficiente de determinação: ", r2)

# comparison = pd.DataFrame({"Real": y_test.values, "Previsto": y_pred})

# print(comparison.head(10))
# print(model.coef_)
# print(X.head(1))

