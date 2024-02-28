# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import warnings

# Suppress the scikit-learn warning about feature names
warnings.filterwarnings("ignore", category=UserWarning)

# Define a dictionary 'data' with 'Hours_Study' and 'Exam_Score'
data = {
    'Hours_Study': [2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Score': [50, 60, 70, 75, 80, 85, 80, 92, 95]
}

# Create a DataFrame 'df' from the 'data' dictionary with named columns
df = pd.DataFrame(data, columns=['Hours_Study', 'Exam_Score'])

# Create variables 'x' and 'y' representing feature and target columns from the DataFrame 'df'
x = df[['Hours_Study']]
y = df[['Exam_Score']]

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create an instance of the Linear Regression model
model = LinearRegression()

# Fit the Linear Regression model to the training data
model.fit(x_train, y_train)

# Prompt the user to enter the number of hours they study
user_input = float(input("Enter the number of hours you study: "))

# Use the trained model to predict the exam score based on the user's input
predicted_score = model.predict([[user_input]])

# Print the predicted exam score based on the user's input
print(f"Predicted Exam Score: {predicted_score[0][0]:.2f}")
