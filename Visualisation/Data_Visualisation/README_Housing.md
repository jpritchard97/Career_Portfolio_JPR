# London Housing Dataset Analysis

## Overview

This repository contains data and analysis related to housing in London. The dataset includes historical prices, sales, crimes, resident satisfaction, and salaries by borough. The analysis aims to provide insights into the London housing market dynamics and related factors.

## Dataset Information

The dataset comprises several variables:

- Monthly average house prices
- Yearly number of houses
- Yearly median salary of residents by area
- Yearly mean salary of residents by area
- Monthly number of crimes committed
- Yearly number of jobs

## Data Processing and Cleaning

The initial steps involve data processing and cleaning using Python libraries such as pandas and numpy. Missing values are handled, and columns with less than 5% null values are retained. Forward fill (ffill) is used to replace missing values with the last valid observation.

## Analysis Objectives

1. Investigate the trend of average housing prices over time.
2. Explore the relationship between average housing prices and other variables like salaries and crimes.
3. Predict future housing price trends using machine learning models.

## Key Findings

- The average housing prices in London have shown an increasing trend over the years.
- There is a moderate correlation between average housing prices and median/mean salaries of residents.
- Machine learning models predict future housing price trends with a certain degree of accuracy.

## Visualizations

- Line plot depicting the trend of average housing prices over time.
- Scatter plots to visualize the relationship between housing prices and other variables.
- Regression analysis for predicting future housing price trends.

## Conclusion

The analysis provides valuable insights into the London housing market, helping stakeholders make informed decisions. Understanding the factors influencing housing prices can aid policymakers, real estate developers, and residents in navigating the dynamic housing landscape of London.

For detailed code and analysis, please refer to the Jupyter Notebook provided in this repository.
