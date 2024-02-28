import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import warnings

# Suppress the scikit-learn warning about feature names
warnings.filterwarnings("ignore", category=UserWarning)

data = np.array(
    [[25, 50000, 2],
     [30, 80000, 1],
     [35, 60000, 3],
     [20, 30000, 2],
     [40, 90000, 1],
     [45, 75000, 2]])

labels = np.array([1, 2, 1, 0, 2, 1])  # 0: Low, 1: Medium, 2: High

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train_scaled, y_train)

accuracy = knn.score(x_test_scaled, y_test)
print(f"Model Accuracy: {accuracy}")

age = int(input("Enter the Age: "))
salary = int(input("Enter the Salary: "))
item = int(input("Enter the No of Buying Items: "))
user_data = np.array([[age, salary, item]])
user_data_scaled = scaler.transform(user_data)
prediction = knn.predict(user_data_scaled)

if prediction[0] == 1:
    print('Medium')
elif prediction[0] == 0:
    print("Low")
else:
    print("High")
