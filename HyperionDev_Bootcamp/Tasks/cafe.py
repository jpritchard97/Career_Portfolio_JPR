'''
start
import pandas
display menu
Assign dictionaries for stock and price
Use pandas to loop through dictionary
Calculate, print value
'''
# Import pandas to use instead of loops
import pandas as pd

# menu list creation, initilization of lists for stock and price
menu = ['coffee', 'tea', 'soup', 'cake']
stock_choice = []
price_choice = []

# Stock dictionary
stock = {
    'coffee': 0.50,
    'tea': 0.30,
    'soup': 0.20,
    'cake': 0.50
}
# price dictionary
price = {
    'coffee': 3.50,
    'tea': 2.50,
    'soup': 4.20,
    'cake': 1.80
}

#print(stock)
#print(price)

# pandas to loop through both stock and price
stock_series = pd.Series(stock)
price_series = pd.Series(price)

# Total calculations using sum()
total_stock = stock_series.sum()
total_price = price_series.sum()

'''print("Total Stock", total_stock)
print("Total price", total_price)'''

# * operator to gain item value
# print w/ f-string
item_value = (total_stock * total_price)
print(f"The total stock worth in the cafe is £{item_value:.2f}") # 2 decimal places
