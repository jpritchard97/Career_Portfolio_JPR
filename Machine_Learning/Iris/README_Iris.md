# Iris Dataset Analysis

## Overview
This repository contains Python code for analyzing the Iris dataset using logistic regression. The analysis includes data preprocessing, model training, evaluation, and performance metrics calculation.

## Libraries Used
- `numpy` and `pandas` for data manipulation
- `matplotlib.pyplot` for data visualization
- `sklearn` for dataset loading, train-test splitting, logistic regression modeling, and performance metrics calculation

## Data Preparation
The Iris dataset is loaded using the `load_iris` function from `sklearn.datasets`. Features and target variables are extracted from the dataset, and data scaling is performed using `preprocessing.scale`.

## Model Training
Logistic regression model is trained on the scaled data using `LogisticRegression` from `sklearn.linear_model`.

## Model Evaluation and Performance Metrics
### Accuracy Score
The accuracy score of the model is calculated using the `score` method from `LogisticRegression`. An accuracy score of 0.9736842105263158 is achieved.

### Confusion Matrix
A confusion matrix is generated using the `confusion_matrix` function from `sklearn.metrics`. The matrix shows the counts of true positive, false positive, true negative, and false negative predictions for each class.

### F1 Score
The F1 score is calculated using the `f1_score` function from `sklearn.metrics`. Both the average F1 score and per-class F1 scores are computed. The average F1 score is 0.9736842105263158, and the hardest class to classify is 'virginica'.

### Precision and Recall
Precision and recall scores for the 'virginica' class are calculated using the `precision_score` and `recall_score` functions from `sklearn.metrics`. The precision score is 0.9, and the recall score is 1.0 for the 'virginica' class.

## Conclusion
This README provides an overview of the code and its functionalities for analyzing the Iris dataset using logistic regression. The analysis includes model training, evaluation, and performance metrics calculation.
