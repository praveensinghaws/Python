# Import necessary libraries
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Read the dataset into a DataFrame
df = pd.read_csv("Screentime-App-Details-Dataset.csv")

# Display the first few rows of the DataFrame
print("First Few Rows:")
print(df.head())

# Display the number of missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Display summary statistics of numeric columns
print("\nSummary Statistics:")
print(df.describe())

# Create a bar chart for Usage by Date and App
figure = px.bar(data_frame=df, x="Date", y="Usage", color="App", title="Usage Graph by Praveen Singh")
figure.show()

# Create a bar chart for Notifications by Date and App
figure = px.bar(data_frame=df, x="Date", y="Notifications", color="App", title="Notifications Graph by Praveen Singh")
figure.show()

# Create a bar chart for Times opened by Date and App
figure = px.bar(data_frame=df, x="Date", y="Times opened", color="App", title="Times opened Graph by Praveen Singh")
figure.show()

# Create a scatter plot for the relationship between Number of Notifications and Usage
figure = px.scatter(data_frame=df, x="Notifications", y="Usage", size="Notifications", trendline="ols",
                    title="Relationship Between Number of Notifications and Amount of Usage")
figure.show()
