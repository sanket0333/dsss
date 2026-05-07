import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')

missing_values = df.isnull().sum()
print("Missing Values in each column:\n", missing_values)

data_description = df.describe()
print("Initial Statistics:\n", data_description)

print("Data Types:\n", df.dtypes)

print("Shape of the data:", df.shape)


print(df.dtypes)

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

df['Survived'] = df['Survived'].astype('category')

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

print("Data Types After Conversion:\n", df.dtypes)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)