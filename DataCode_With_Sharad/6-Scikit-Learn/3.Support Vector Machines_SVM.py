# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import warnings

data = {
    "Age": [30, 25, 35, 20, 40, 55, 32, 28],
    "Monthly_Recharge": [50, 60, 80, 40, 100, 120, 70, 55],
    "Churn": [0, 1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
print(df)

x = df[['Age', 'Monthly_Recharge']]
y = df[['Churn']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model_SVC = SVC(kernel='linear', C=1.0)  # Default regularization
model_SVC.fit(x_train, y_train)

y_prediction = model_SVC.predict(x_test)
accuracy = accuracy_score(y_test, y_prediction)
print(accuracy)
report = classification_report(y_test, y_prediction)
print(report)

user_age = float(input("Enter customer's Age: "))
user_Monthly_Recharge = int(input("Enter customer monthly Recharge: "))

user_input_data = np.array([[user_age, user_Monthly_Recharge]])

prediction = model_SVC.predict(user_input_data)
if prediction[0] == 0:
    print("The Customer is at risk of churning.")
else:
    print("The Customer is likely to stay.")
