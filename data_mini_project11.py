# -*- coding: utf-8 -*-
"""DATA-mini-project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HuVoklsSWyLMsab9Z82wPl0s4TQFE6pZ

**Loading Packages and Data**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""**data loading**"""

from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

import pandas as pd

# File paths for the CSV files
train_csv_path = '/content/drive/MyDrive/Train.csv'
test_csv_path = '/content/drive/MyDrive/Test.csv'

# Load CSV files using pandas
train_data = pd.read_csv(train_csv_path)
test_data = pd.read_csv(test_csv_path)

"""**Data stucter and containt**"""

# Check the number of rows and columns in the dataset
print("Data Shape:")
print("Train Data:", train_data.shape)
print("Test Data:", test_data.shape)

# Check the data types of each column
print("\nData Types:")
print(train_data.dtypes)

# Get summary statistics for numerical columns
print("\nSummary Statistics:")
print(train_data.describe())

# Display a few rows of the dataset
print("\nSample Data:")
print(train_data.head())

"""**Exploratory Data Analysis EDA**

data visualization
"""

# Plot histogram of the target variable (Item_Outlet_Sales)
plt.figure(figsize=(8, 5))
sns.histplot(train_data['Item_Outlet_Sales'], kde=True)
plt.title('Distribution of Item Outlet Sales')
plt.xlabel('Item Outlet Sales')
plt.ylabel('Frequency')
plt.show()

# Plot box plots for numerical variables to identify outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=train_data.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1))
plt.title('Box Plot of Numerical Variables')
plt.xticks(rotation=45)
plt.show()

# Plot bar plots for categorical variables
categorical_columns = train_data.select_dtypes(include='object').columns
plt.figure(figsize=(14, 12))
for i, col in enumerate(categorical_columns):
    plt.subplot(3, 3, i + 1)
    sns.countplot(x=col, data=train_data)
    plt.title(f'{col} Distribution')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Outlier Detection using IQR method
def detect_outliers_iqr(data, col, threshold=1.5):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
    return outliers

# Detect outliers in the 'Item_Outlet_Sales' column
outliers_sales = detect_outliers_iqr(train_data, 'Item_Outlet_Sales', threshold=1.5)
print("Outliers in Item_Outlet_Sales:")
print(outliers_sales)

# Detect outliers in the 'Item_Weight' column
outliers_weight = detect_outliers_iqr(train_data, 'Item_Weight', threshold=1.5)
print("Outliers in Item_Weight:")
print(outliers_weight)

#Detect outliers in the 'Item_Visibility' column
outliers_visibility = detect_outliers_iqr(train_data, 'Item_Visibility', threshold=1.5)
print("Outliers in Item_Visibility:")
print(outliers_visibility)

# Detect outliers in the 'Item_MRP' column
outliers_mrp = detect_outliers_iqr(train_data, 'Item_MRP', threshold=1.5)
print("Outliers in Item_MRP:")
print(outliers_mrp)

#Detect outliers in the 'Item_Weight' column for a higher threshold (more extreme outliers)
outliers_weight_extreme = detect_outliers_iqr(train_data, 'Item_Weight', threshold=3)
print("Extreme Outliers in Item_Weight:")
print(outliers_weight_extreme)

"""**Corrolation matrix**"""

correlation_matrix = train_data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

"""**Univariate Analysis**"""

plt.figure(figsize=(8, 6))
plt.hist(train_data['Item_MRP'], bins=30, edgecolor='k')
plt.xlabel('Item MRP')
plt.ylabel('Frequency')
plt.title('Histogram of Item MRP')
plt.show()

print("Summary Statistics for Item MRP:")
print(train_data['Item_MRP'].describe())

plt.figure(figsize=(8, 6))
plt.hist(train_data['Item_Weight'], bins=30, edgecolor='k')
plt.xlabel('Item Weight')
plt.ylabel('Frequency')
plt.title('Histogram of Item Weight')
plt.show()
print("Summary Statistics for Item Weight:")
print(train_data['Item_Weight'].describe())

plt.figure(figsize=(8, 6))
plt.hist(train_data['Item_Fat_Content'], bins=30, edgecolor='k')
plt.xlabel('Item Fat_Content')
plt.ylabel('Frequency')
plt.title('Histogram of Item Fat_Content')
plt.show()
print("Summary Statistics for Item Fat_Content:")
print(train_data['Item_Fat_Content'].describe())

size_mapping = {'Small': 1, 'Medium': 2, 'High': 3}
train_data['Outlet_Size_numeric'] = train_data['Outlet_Size'].map(size_mapping)

plt.figure(figsize=(8, 6))
plt.hist(train_data['Outlet_Size_numeric'], bins=30, edgecolor='k')
plt.xlabel('Outlet Size (Numeric)')
plt.ylabel('Frequency')
plt.title('Histogram of Outlet Size (Numeric)')
plt.show()

"""**Bivariate Analysis**"""

#Bivariate Analysis between 'Item_MRP' and 'Item_Outlet_Sales'
plt.figure(figsize=(8, 6))
plt.scatter(train_data['Item_MRP'], train_data['Item_Outlet_Sales'], alpha=0.5)
plt.xlabel('Item MRP')
plt.ylabel('Item Outlet Sales')
plt.title('Scatter plot: Item MRP vs. Item Outlet Sales')
plt.show()

# Correlation between 'Item_MRP' and 'Item_Outlet_Sales'
correlation = train_data['Item_MRP'].corr(train_data['Item_Outlet_Sales'])
print("Correlation between Item MRP and Item Outlet Sales:", correlation)

#Bivariate Analysis between 'Item_Weight' vs. 'Item_Outlet_Sales'
plt.figure(figsize=(8, 6))
plt.scatter(train_data['Item_Weight'], train_data['Item_Outlet_Sales'], alpha=0.5)
plt.xlabel('Item Weight')
plt.ylabel('Item Outlet Sales')
plt.title('Scatter plot: Item Weight vs. Item Outlet Sales')
plt.show()

# Correlation between 'Item_Weight' vs. 'Item_Outlet_Sales'
correlation = train_data['Item_Weight'].corr(train_data['Item_Outlet_Sales'])
print("Correlation between Item Weight and Item Outlet Sales:", correlation)

# Bivariate Analysis between 'Item_Visibility' and 'Item_Outlet_Sales'
plt.figure(figsize=(8, 6))
plt.scatter(train_data['Item_Visibility'], train_data['Item_Outlet_Sales'], alpha=0.5)
plt.xlabel('Item Visibility')
plt.ylabel('Item Outlet Sales')
plt.title('Scatter plot: Item Visibility vs. Item Outlet Sales')
plt.show()

# Correlation between 'Item_Visibility' and 'Item_Outlet_Sales'
correlation = train_data['Item_Visibility'].corr(train_data['Item_Outlet_Sales'])
print("Correlation between Item Visibility and Item Outlet Sales:", correlation)

"""**Multivariat plot**"""

plt.figure(figsize=(8, 6))
sns.barplot(x='Item_Type', y='Item_Outlet_Sales', data=train_data, palette='gist_rainbow_r')
plt.xlabel('Item_Type', fontsize=14)
plt.xticks(rotation=90)
plt.ylabel('Item Outlet Sales', fontsize=14)
plt.show()

"""**Missing Value Treatment**"""

# Impute missing values for Item_Weight with mean
train_data['Item_Weight'].fillna(train_data['Item_Weight'].mean(), inplace=True)

# Impute missing values for Outlet_Size with mode
train_data['Outlet_Size'].fillna(train_data['Outlet_Size'].mode()[0], inplace=True)

train_data['Outlet_Size'].fillna(train_data['Outlet_Size'].mode()[0], inplace=True)

size_mapping = {'Small': 1, 'Medium': 2, 'High': 3}

train_data['Outlet_Size_numeric'] = train_data['Outlet_Size'].map(size_mapping)

print("Columns with Missing Values after Treatment:")
print(train_data.isnull().sum())

"""**Feature engineering**

Let's drop Outlet_Establishment_Year, Item_Identifier and Outlet_Identifier because they don't have significant values.
"""

train_data = pd.read_csv(train_csv_path)
train_data.drop(columns=['Outlet_Establishment_Year', 'Item_Identifier', 'Outlet_Identifier'], inplace=True)

"""Laabel encoding for ordinal variables:"""

from sklearn.preprocessing import LabelEncoder

ordinal_columns = ['Item_Fat_Content', 'Outlet_Size']

le = LabelEncoder()
for col in ordinal_columns:
    train_data[col] = le.fit_transform(train_data[col])

"""
One-hot encoding for categorical variables
"""

# Perform one-hot encoding only if it wasn't done before
if 'Outlet_Type_Supermarket Type1' not in train_data.columns:
    train_data = pd.get_dummies(train_data, columns=['Outlet_Type'], prefix_sep='')

if 'Item_Type_Breads' not in train_data.columns:
    train_data = pd.get_dummies(train_data, columns=['Item_Type'], prefix_sep='')

# Print the new columns after one-hot encoding
print(train_data.columns)

"""Verify the updated dataset

"""

print(train_data.head())

"""**Modeling**

**Linear regretion**
"""

# Convert categorical variables to numerical using one-hot encoding
train_data = pd.get_dummies(train_data, drop_first=True)

# Handle missing values (if any) in numerical columns
train_data['Item_Weight'].fillna(train_data['Item_Weight'].mean(), inplace=True)

# Split the data into features (X) and target variable (y)
X = train_data.drop('Item_Outlet_Sales', axis=1)
y = train_data['Item_Outlet_Sales']

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the linear regression model
linear_model = LinearRegression()

# Fit the model on the training data
linear_model.fit(X_train, y_train)

# Get the coefficients and intercept of the model
coefficients = linear_model.coef_
intercept = linear_model.intercept_

# Print the coefficients and intercept
print("Coefficients:", coefficients)
print("Intercept:", intercept)

# Make predictions on the test data
y_pred = linear_model.predict(X_test)

# Evaluate the model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print("R-squared:", r2)


# Create a DataFrame with the predictions
df_predictions = pd.DataFrame({'Item_Outlet_Sales_Predicted': y_pred})

# Merge the predictions DataFrame with the original test DataFrame
df_merged = pd.concat([test_data, df_predictions], axis=1)
df_merged = df_merged[['Item_Identifier', 'Outlet_Identifier', 'Item_Outlet_Sales_Predicted']]

# Save the merged DataFrame to a CSV file
df_merged.to_csv('predictions.csv', index=False)

# Download the CSV file
from google.colab import files
files.download('predictions.csv')

"""**Regularized Linear Regression**

Ridge Regression
"""

from sklearn.linear_model import Ridge

# Initialize the Ridge Regression model
ridge_model = Ridge(alpha=0.05)  # You can adjust the alpha (regularization strength)

# Fit the model on the training data
ridge_model.fit(X_train, y_train)

# Get the coefficients and intercept of the model
coefficients_ridge = ridge_model.coef_
intercept_ridge = ridge_model.intercept_

# Print the coefficients and intercept
print("Ridge Coefficients:", coefficients_ridge)
print("Ridge Intercept:", intercept_ridge)

# Make predictions on the test data
y_pred_ridge = ridge_model.predict(X_test)

# Evaluate the model
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
print("Ridge Mean Squared Error:", mse_ridge)

mae_ridge = mean_absolute_error(y_test, y_pred_ridge)
print("Ridge Mean Absolute Error:", mae_ridge)

r2_ridge = r2_score(y_test, y_pred_ridge)
print("Ridge R-squared:", r2_ridge)

# Create a DataFrame with the predictions
df_predictions_ridge = pd.DataFrame({'Item_Outlet_Sales_Predicted_Ridge': y_pred_ridge})

# Merge the predictions DataFrame with the original test DataFrame
df_merged_ridge = pd.concat([test_data, df_predictions_ridge], axis=1)
df_merged_ridge = df_merged_ridge[['Item_Identifier', 'Outlet_Identifier', 'Item_Outlet_Sales_Predicted_Ridge']]

# Save the merged DataFrame to a CSV file
df_merged_ridge.to_csv('predictions_ridge.csv', index=False)

# Download the CSV file
from google.colab import files
files.download('predictions_ridge.csv')

"""Lasso Regression"""

from sklearn.linear_model import Lasso

# Initialize the Lasso Regression model
lasso_model = Lasso(alpha=0.05)  # You can adjust the alpha (regularization strength)

# Fit the model on the training data
lasso_model.fit(X_train, y_train)

# Get the coefficients and intercept of the model
coefficients_lasso = lasso_model.coef_
intercept_lasso = lasso_model.intercept_

# Print the coefficients and intercept
print("Lasso Coefficients:", coefficients_lasso)
print("Lasso Intercept:", intercept_lasso)

# Make predictions on the test data
y_pred_lasso = lasso_model.predict(X_test)

# Evaluate the model
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
print("Lasso Mean Squared Error:", mse_lasso)

mae_lasso = mean_absolute_error(y_test, y_pred_lasso)
print("Lasso Mean Absolute Error:", mae_lasso)

r2_lasso = r2_score(y_test, y_pred_lasso)
print("Lasso R-squared:", r2_lasso)

# Create a DataFrame with the predictions
df_predictions_lasso = pd.DataFrame({'Item_Outlet_Sales_Predicted_Lasso': y_pred_lasso})

# Merge the predictions DataFrame with the original test DataFrame
df_merged_lasso = pd.concat([test_data, df_predictions_lasso], axis=1)
df_merged_lasso = df_merged_lasso[['Item_Identifier', 'Outlet_Identifier', 'Item_Outlet_Sales_Predicted_Lasso']]

# Save the merged DataFrame to a CSV file
df_merged_lasso.to_csv('predictions_lasso.csv', index=False)

# Download the CSV file
from google.colab import files
files.download('predictions_lasso.csv')

"""**Random Forest**"""

from sklearn.ensemble import RandomForestRegressor

# Initialize the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model on the training data
rf_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred_rf = rf_model.predict(X_test)

# Evaluate the model
mse_rf = mean_squared_error(y_test, y_pred_rf)
print("Random Forest Mean Squared Error:", mse_rf)

mae_rf = mean_absolute_error(y_test, y_pred_rf)
print("Random Forest Mean Absolute Error:", mae_rf)

r2_rf = r2_score(y_test, y_pred_rf)
print("Random Forest R-squared:", r2_rf)

# Create a DataFrame with the predictions
df_predictions_rf = pd.DataFrame({'Item_Outlet_Sales_Predicted_RF': y_pred_rf})

# Merge the predictions DataFrame with the original test DataFrame
df_merged_rf = pd.concat([test_data, df_predictions_rf], axis=1)
df_merged_rf = df_merged_rf[['Item_Identifier', 'Outlet_Identifier', 'Item_Outlet_Sales_Predicted_RF']]

# Save the merged DataFrame to a CSV file
df_merged_rf.to_csv('predictions_rf.csv', index=False)

# Download the CSV file
from google.colab import files
files.download('predictions_rf.csv')