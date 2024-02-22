'''
Start
prompt user for input: "Enter your age: "
store input as an integer, via "age"
Logic order
    Oldest to youngest
Initial if statement
elif statements (no multiple output statments)
else statement to finish string
End
'''

# Assign variable to input users name
# int() used to remove possibility of float output
age = int(input("Enter your age: "))

# Logic order, oldest age first
# If statement greater than 100
if age > 100:
    print("Sorry, you're dead")

# Elif statement greater or equal to 65
elif  age >= 65:
    print("Enjoy your retirement!")

# Elif statement greater or equal to 40
elif age >= 40:
    print("You're over the hill")

# Elif statement equalling 21
elif age == 21:
    print("Congrats on your 21st!")

# Elif statement less than or equal to 13
elif age < 13:
    print("You qualify for the kiddie discount")

# Ending else statement
else:
    print("Age is but a number")