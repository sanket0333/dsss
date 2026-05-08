
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv('iris.csv', names=column_names)


print(iris_data.head())
print(iris_data.info())
 
print(iris_data.dtypes)
print(iris_data.describe())




iris_data.hist(bins=10, figsize=(10, 8))
plt.suptitle('Histograms of Iris Dataset Features')
plt.show()

plt.figure(figsize=(10, 8))
sns.boxplot(data=iris_data.drop('species', axis=1))
plt.title('Box Plot of Features in the Iris Dataset')
plt.show()


plt.figure(figsize=(12, 8))
for i, feature in enumerate(iris_data.columns[:-1]):
    plt.subplot(2, 2, i + 1)
    sns.histplot(data=iris_data, x=feature, hue="species", kde=True)
    plt.title(f'Distribution of {feature}')

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 8))
for i, feature in enumerate(iris_data.columns[:-1]):
    plt.subplot(2, 2, i + 1)
    sns.boxplot(x='species', y=feature, data=iris_data)
    plt.title(f'Box Plot of {feature} by Species')

plt.tight_layout()
plt.show()