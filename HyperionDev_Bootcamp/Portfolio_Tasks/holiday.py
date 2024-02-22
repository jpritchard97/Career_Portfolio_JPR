'''
start
To calculate a users total holiday cost, which includes plane cost, hotel cost and car-rental cost
1)  User inputs required:
        Options for flights/ destinations (city_flight)
        No. of nights staying at destination (num_nights)
        No. of days for which they will be hiring a car (rental_days)

2)  Creation of functions:
        Cost of the hotel per night (hotel_cost), takes num_nights as argument
        Cost of travel (plane_cost), takes city_flight as an argument
        Cost of car per days rented (car_rental), takes rental days as an argument

3)  Total cost of holiday:
        Uses as arguments:
            hotel_cost
            plane_cost
            car_rental
4)  print the outcome
5)  Try running the programme with different combinations of input to shows its compatibility
end
'''
import tabulate

# Create a dictionary with the locations
# Someone to choose from the list
# Both the key and value will be held in return
# Define a function that holds these values

def city_flights(destination):

    destinations = {
        'London' : 36,
        'Barcelona' : 72,
        'Tokyo' : 650,
        'New York' : 780,
        'Bejing' : 500,
        'Vancover' : 690,
        'Munich' : 150,
        'Copenhagen' : 100
    }

    if destination in destinations:
        return destination, destinations[destination]
    else:
        return None

# Menu of options
print("""
        London     : 36
        Barcelona  : 72
        Tokyo      : 650
        New York   : 780
        Bejing     : 500
        Vancover   : 690
        Munich     : 150
        Copenhagen : 100
""")
# destination input
destination_input = input("Enter your choice of destination from the options above: ")

# Splitting of the key and values in the list
# Call upon the function for a single pairing
destination_key, destination_value_price = city_flights(destination_input)

# if statment if key item is in the dictionary
if destination_key is not None:
    print(f"Destination: {destination_key}, Price: £{destination_value_price:.2f}") # 2. d.p.
else: # Account for error of incorrect key input
    print("Destination not found")

while True: # while loop to allow reentry of input if ValueError is activated
    try: # Account for value error
        num_nights = int(input(f"How many nights will you be staying in {destination_key} : ")) # More user friendly
        print(f"You will be staying in {destination_key} for {num_nights} nights")
        break

    except ValueError:
        print("Incorrect input, please try again")
        continue

rental_choice = input("Will you be requiring a car to hire (y/n): ").lower() # Option of rental car 

# if statement for whether a car is required
if rental_choice.lower() == 'y':  
    rental_days = int(input("How many days will you require this hire: "))

# The rental cannot exceed the number of nights
    if rental_days > num_nights: # New line to create a more easily readable code
        print(f"You cannot hire a car for {rental_days} days,\nthis exceeds the number of nights you will be staying in {destination_key}.")
    else:
        print(f"You will be hiring a car for {rental_days} days.")
else:
    print("No problem! This won't be added to your total cost")
    rental_days = 0 # Set to 0 as holiday_cost function wont operate, error will be found

# disclaimer of hotel cost per night
print("The cost of the hotel per night is £150.00")

# def functions stated in brief
def hotel_cost(num_nights):
    price_per_night = 150
    return price_per_night * num_nights

def car_rental(rental_days):
    price_per_day = 75
    return price_per_day * rental_days

# Total cost function
def holiday_cost(num_nights, rental_days, destination_value_price):
    total_cost_duration = hotel_cost(num_nights)
    total_rental_cost = car_rental(rental_days)
    return destination_value_price + total_cost_duration + total_rental_cost


# Calculate the total holiday cost
total_holiday_cost = holiday_cost(num_nights, rental_days, destination_value_price)
print(f"The total cost for the holiday is: £{total_holiday_cost}")
