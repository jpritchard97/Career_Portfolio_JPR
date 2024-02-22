'''
pseudocode added to organise this chaos
Test code initially to find first error
Find all sources of errors by commenting out areas to see the logical path of errors
label these errors first
change errors
test after each change
look back at error comments, change if needed
final test to see if programme works without logical errors
'''


# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = ("Lion") # Syntax error, missing parentheses, name error as lion was not defined
animal_type = ("cub") # Syntax error, missing parentheses
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth") # Syntax error, missing f-string format. 
# logical error, animal_type and number_of_teeth switched around
# string formatting error

print(full_spec) # Syntax error, missing parentheses