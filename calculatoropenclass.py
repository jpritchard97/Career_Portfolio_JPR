

'''
while True:

    x = float(input("please enter a value: "))
    y = float(input("please enter a value: "))

    total = x + y
    
    print("Here is your calculation: ")
    print(total)

'''



num = int(input("Enter a number you would like for the times table of: "))

# times tables go up to 12

for table in range(1, 13):
    print(f"{num} * {table} = {num * table}")
