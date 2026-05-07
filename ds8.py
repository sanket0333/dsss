
import seaborn as sns
import matplotlib.pyplot as plt



titanic_data = sns.load_dataset('titanic')

print(titanic_data.head())

print(titanic_data.describe())

plt.figure(figsize=(10, 6))
sns.histplot(titanic_data['fare'], kde=True, bins=30, color='blue')

plt.title('Distribution of Ticket Prices (Fare) for Titanic Passengers', fontsize=16)
plt.xlabel('Fare', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True)

plt.show()