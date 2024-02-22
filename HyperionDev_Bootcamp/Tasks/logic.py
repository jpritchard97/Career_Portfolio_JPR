'''
start
logical error - code works but output is not what is expected
simple code ---> average of two numbers, incorrect answer
f-string to concatenate numbers together
end
'''
# Ask user for number inut
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

#average these numbers but divide by incorrect amount
average = (num1 + num2) / 3

# print concatenated string
print(f"The number of {num1} and {num2} is {average}")
