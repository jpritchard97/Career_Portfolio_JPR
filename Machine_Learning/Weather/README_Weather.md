# Weather Data Analysis and Prediction

## Introduction
This project aims to analyze weather data and predict tomorrow's maximum temperature ('tmax') using machine learning techniques. The dataset used in this analysis contains historical weather data from JFK International Airport, NY, US.

## Data Preprocessing
### Importing Libraries and Loading Data
- Imported necessary libraries: `numpy`, `pandas`, `mean_absolute_error` from `sklearn.metrics`, `Ridge` from `sklearn.linear_model`.
- Loaded the weather dataset from 'weather.csv' file and specified the index as 'DATE'.

### Data Cleaning
- Calculated the percentage of null values in each column and filtered out columns with null percentages below 5%.
- Converted column names to lowercase for consistency.
- Forward filled missing values in the dataset.

### Data Processing
- Converted the index of the DataFrame to datetime format.
- Filtered out data from the year 2024.
- Assigned the filtered DataFrame to a new variable 'weather' for further analysis.

## Machine Learning
### Predicting Tomorrow's Maximum Temperature
- Created a target variable for tomorrow's 'tmax' by shifting the 'tmax' column.
- Utilized Ridge Regression model to predict tomorrow's 'tmax'.
- Evaluated the model using Mean Absolute Error (MAE).

## Results and Analysis
### Model Evaluation
- Calculated Mean Absolute Error (MAE) of the predictions.
- Observed that, on average, the model's predictions are within +/- 5 degrees Celsius of the actual values.

### Observations
- The model tends to have larger errors during certain periods.

## Conclusion
The analysis provides insights into historical weather patterns and demonstrates the potential of machine learning models in weather prediction. Further improvements can be made by refining feature engineering and exploring alternative models.

