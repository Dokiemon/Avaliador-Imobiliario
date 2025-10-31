import sklearn
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = fetch_california_housing(as_frame=True)
df = data.frame
X = df.drop(columns = "MedHouseVal") #o X aramzena todas as colunas do dataframe exceto (drop) a coluna alvo (MedHouseVal)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = LinearRegression() #criou o objeto
model.fit(X_train, y_train) #treinou o objeto

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Taxa Erro Médio Absoluto: ", mae)
print("Taxa Erro Médio Quadrático: ", mse)
print("Coeficiente de determinação: ", r2)

comparison = pd.DataFrame({f"Real: {y_test}\nPrevisto: {y_pred}"})

print(comparison)