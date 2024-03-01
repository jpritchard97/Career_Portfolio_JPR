# Data Manipulation and Linear Regression Modelling

## Overview
This repository contains code for data manipulation, visualisation, and building linear regression models to analyse the relationship between age and charges in an insurance dataset.

## Libraries Used
- `numpy` and `pandas` for data manipulation
- `matplotlib.pyplot` and `seaborn` for data visualisation
- `sklearn` for train-test dataset splitting and linear regression modelling
- `statsmodels.api` for Ordinary Least Squares (OLS) regression modelling

## Data Cleaning and Processing
The dataset used in this analysis is 'insurance.csv'. Data cleaning and preprocessing steps include:
- Checking for missing values and dropping any rows with missing values.
- Removing duplicate entries.
- Identifying target variables ('age' and 'charges').

## Scatter Plot Visualisation
A scatter plot with 'age' on the x-axis and 'charges' on the y-axis is created using `matplotlib.pyplot` and `seaborn`. Differentiation by 'smoker' status is incorporated using colour ('hue'). The plot helps visualise the relationship between age, charges, and smoking status.

## Linear Regression Modeling
Linear regression models are built using `sklearn.linear_model.LinearRegression` and `statsmodels.api.OLS`. The steps include:
- Splitting the dataset into training and testing sets.
- Training the model using the training data.
- Making predictions on the test data.
- Evaluating the model using Mean Squared Error (MSE) and R^2 Score.
- Implementing an OLS regression model with additional statistical insights.

## Evaluation Metrics
Evaluation metrics such as Mean Squared Error (MSE) and R^2 Score are calculated to assess the accuracy of the linear regression models.

## Improvement and Optimisation
Suggestions for improving and optimising the models include:
- Checking and correcting any issues with the data, such as outliers or missing values.
- Transforming variables to reduce non-normality.
- Exploring different regression models for better performance, such as robust regression or generalised linear models.

## Conclusion
This README provides an overview of the code and its functionalities. Further optimisation and exploration can be conducted to enhance the accuracy and insights of the linear regression models.
