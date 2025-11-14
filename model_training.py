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
    # if data.loc[i, "hoa"]:
    #     if "R$" in data.loc[i, "hoa"]:
    #         data.loc[i, "hoa"] = data.loc[i, "hoa"].replace("R$", "")
    #         data.loc[i, "hoa"] = data.loc[i, "hoa"].replace(",", ".")
    #     if data.loc[i, "hoa"] == "Sem info":
    #         data.loc[i, "hoa"] = 0
    #     if data.loc[i, "hoa"] == "Incluso":
    #         data.loc[i, "hoa"] = 0
    # if data.loc[i, "rent amount"]:
    #     if "R$" in data.loc[i, "rent amount"]:
    #         data.loc[i, "rent amount"] = data.loc[i, "rent amount"].replace("R$", "")
    #         data.loc[i, "rent amount"] = data.loc[i, "rent amount"].replace(",", ".")
    #     if data.loc[i, "rent amount"] == "Incluso":
    #         data.loc[i, "rent amount"] = 0
    # if data.loc[i, "property tax"]:
    #     if "R$" in data.loc[i, "property tax"]:
    #         data.loc[i, "property tax"] = data.loc[i, "property tax"].replace("R$", "")
    #         data.loc[i, "property tax"] = data.loc[i, "property tax"].replace(",", ".")
    #     if data.loc[i, "property tax"] == "Incluso":
    #         data.loc[i, "property tax"] = 0
    # if data.loc[i, "fire insurance"]:
    #     if "R$" in data.loc[i, "fire insurance"]:
    #         data.loc[i, "fire insurance"] = data.loc[i, "fire insurance"].replace("R$", "")
    #         data.loc[i, "fire insurance"] = data.loc[i, "fire insurance"].replace(",", ".")
    #     if data.loc[i, "fire insurance"] == "Incluso":
    #         data.loc[i, "fire insurance"] = 0
    if data.loc[i, "total"]:
        if "R$" in data.loc[i, "total"]:
            data.loc[i, "total"] = data.loc[i, "total"].replace("R$", "")
            data.loc[i, "total"] = data.loc[i, "total"].replace(",", "")

data["floor"] = data["floor"].astype(int)
data["animal"] = data["animal"].astype(int)
data["furniture"] = data["furniture"].astype(int)
# data["hoa"] = data["hoa"].astype(float)
# data["rent amount"] = data["rent amount"].astype(float)
# data["property tax"] = data["property tax"].astype(float)
# data["fire insurance"] = data["fire insurance"].astype(float)
data["total"] = data["total"].astype(float)
data = data.drop(columns = ["city", "hoa", "rent amount", "property tax", "fire insurance"])
print("-------------------")
print(data.dtypes)
X = data.drop(columns = "total") #o X aramzena todas as colunas do dataframe exceto (drop) a coluna alvo (MedHouseVal)
y = data["total"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.05, random_state = 42)

model = LinearRegression() #criou o objeto
model.fit(X_train, y_train) #treinou o objeto

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Taxa Erro Médio Absoluto: ", mae)
print("Taxa Erro Médio Quadrático: ", mse)
print("Coeficiente de determinação: ", r2)

comparison = pd.DataFrame({"Real": y_test.values, "Previsto": y_pred})

print(comparison.head(10))
print(model.coef_)
print(X.head(1))

def predict_rent(user_features):
    predicted_rent = model.predict(user_features)
    return predicted_rent