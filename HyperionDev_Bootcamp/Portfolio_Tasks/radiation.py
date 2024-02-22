'''
1. Import the math library.
2. Create a dictionary 'locations' with different areas as keys and lists of radiation values as values.
3. Define a function 'cal_average' to calculate the average of a list:
    - Take a list as an input and return the average of the list.
4. Define a function 'standard_deviation' to calculate standard deviations for each area in the dictionary:
    - take a dictionary as an input.
    - For each area in the dictionary, calculate the mean and standard deviation.
    - Store the standard deviation in a new dictionary.
    - Return.
5. Print the names of all areas from the 'locations' dictionary.
6. Ask the user to input a location name and store this input.
7. If the entered location is in the dictionary:
    - Print the average radiation value for this location.
    - Print the standard deviation for this location.
8. If the entered location is not in the dictionary, print "Location not found."
9. Create an empty list 'measurements' for additional radiation level inputs.
10. Continuously ask the user to input radiation levels until they enter 'done':
    - Add each entered level to the 'measurements' list.
11. Calculate and print the mean and standard deviation of the values in 'measurements'.
'''
# import statistics as st
import math

# Define the dictionary

locations = {'City Centre' : [22, 19, 20, 31, 28],
            'Industrial Zone' :[35, 32, 30, 30, 37, 40],
            'Residential District' : [15, 12, 18, 20, 14],
            'Rural Outskirts' : [9, 13, 16, 14, 7],
            'Downtown' : [25, 18, 22, 21, 26]
            }

# print(locations), check to debug the dictionary
# locations = key(location) : value(radiation values)

# defining average calculation
def cal_average(levels):
    return sum(levels) / len(levels)

# This is the basis of the defined sd functiom
# Use of a for loop to achieve this
# print(f"Standard Deviation of sample is: {st.stdev(levels)}")

def standard_deviation(dictionary):
    if len(dictionary) == 0:
        return None # Handle the case of an empty dictionary

# initilize dictionary
    std_deviations = {}

    for location, values in dictionary.items():

# sd calculation in steps, numpy could also be used
        mean = cal_average(values)

        squared_diffs = [(x - mean) ** 2 for x in values]

        variance = sum(squared_diffs) / (len(values) - 1)

        std_deviation = math.sqrt(variance)

        std_deviations[location] = std_deviation

# return caluclation back to the user
    return std_deviations

# List all key elements
keys = locations.keys()
for key in keys:
    print(key)

# Ask for input on which location they want the calculations of
# if statement to print both calulations to input response
location_choice = input("Enter a location: ").strip().lower()

# To make sure input can be entered as lowercase and still be recognised
if location_choice in [key.lower() for key in locations]:
    chosen_location = None
    for key in locations: # for loop to iterate over the keys in dictionary
        if key.lower() == location_choice:
            chosen_location = key
            break

    levels = locations[chosen_location]
    print(f"{chosen_location} average radiation value = {cal_average(levels)}")
    std_deviations = standard_deviation(locations)
    print(f"{chosen_location} Standard Deviation = {std_deviations[chosen_location]:.2f}")
else:
    print("Location not found.")


# initilize list
measurements = []

# while loop whilst input is True
# Ask for input for int values
while True:
    level = input("Enter radiation level or 'done' to finish: ").lower()

    if level.lower() == "done":
        break
    try: # append int values to list
        measurements.append(int(level))
    except ValueError:
        print("Invalid input: {level}")

# return average from defined function
mean = cal_average(measurements)
std_deviation = math.sqrt(sum((x - mean) ** 2 for x in measurements) / (len(measurements) - 1))

if mean is not None:
    print("Mean:", mean)
else:
    print("No measurements to calculate the mean.")

print("Standard Deviation: {:.2f}".format(std_deviation)) # 2dp using .format() rather than f string
