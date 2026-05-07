import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score 
import seaborn as sns 
import matplotlib.pyplot as plt
 
column_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'] 
dataset = df = pd.read_csv('iris.csv', header=None, names=column_names)

X = dataset.iloc[:, :-1].values   
y = dataset.iloc[:, -1].values   
 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
 

model = GaussianNB() 
model.fit(X_train, y_train) 
 

y_pred = model.predict(X_test)

 
cm = confusion_matrix(y_test, y_pred) 
accuracy = accuracy_score(y_test, y_pred) 
precision = precision_score(y_test, y_pred, average='weighted') 
recall = recall_score(y_test, y_pred, average='weighted') 
error_rate = 1 - accuracy 
 
print("Confusion Matrix:\n", cm) 
print(f"Accuracy: {accuracy}") 
print(f"Precision: {precision}") 
print(f"Recall: {recall}") 
print(f"Error Rate: {error_rate}") 




sns.heatmap(cm, annot=True,  cmap='Blues', xticklabels=model.classes_, 
yticklabels=model.classes_) 
plt.xlabel('Predicted') 
plt.ylabel('Actual') 
plt.title('Confusion Matrix') 
plt.show() 
