import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score 


columns = [ 'CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 
'LSTAT', 'MEDV'] 
df = pd.read_csv('housing.csv') 
 
 

print(df.isnull().sum()) 
print(df.head())
df = df.dropna()


plt.figure(figsize=(10,8)) 
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5) 
plt.title("Correlation Matrix") 
plt.show()


X = df.drop('MEDV', axis=1)
y = df['MEDV']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")

print(f"R-squared: {r2}")

plt.figure(figsize=(8,6)) 
plt.scatter(y_test, y_pred, color='blue') 
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2) 
plt.title("Predicted vs Actual Prices") 
plt.xlabel("Actual Prices") 
plt.ylabel("Predicted Prices") 
plt.show() 
