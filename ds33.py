import pandas as pd
import numpy as np


column_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']


df = pd.read_csv('iris.csv', header=None, names=column_names)


setosa = df[df['Species'] == 'Iris-setosa']
versicolor = df[df['Species'] == 'Iris-versicolor']
virginica = df[df['Species'] == 'Iris-virginica']


print("Iris-setosa Statistics:\n")
print(setosa.describe())

print("\nIris-versicolor Statistics:\n")
print(versicolor.describe())

print("\nIris-virginica Statistics:\n")
print(virginica.describe())



import matplotlib.pyplot as plt 
import seaborn as sns 
 

sns.histplot(setosa['SepalLength'], kde=True) 
plt.title('Distribution of Sepal Length (Iris-setosa)') 
plt.show()
