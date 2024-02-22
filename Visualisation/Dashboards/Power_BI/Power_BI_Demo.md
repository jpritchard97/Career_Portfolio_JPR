# Sales Dashboard Data

This dataset contains sales information for various beverage brands across different retailers, regions, states, and months. The dataset includes the following fields:

- `Retailer`: The name of the retailer.
- `Retailer ID`: A unique identifier for the retailer.
- `Date`: The date of the sale.
- `Month`: The month of the sale (1-12).
- `Region`: The region of the retailer.
- `State`: The state where the retailer is located.
- `Beverage Brand`: The brand of the beverage sold.
- `Price per Unit`: The price per unit of the beverage.
- `Units Sold`: The number of units sold.

## Data Analysis with Python

To analyze the dataset, we can use the `pandas` library to read and manipulate the data. Here's an example of how to read the dataset using pandas:

```python
import pandas as pd

sales_data = pd.read_csv('sales_dashboard_data.csv')
