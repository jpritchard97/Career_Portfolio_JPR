'''
Nizaam will run through the Capstone project
He will give us hints to help us on this

Criteria for the first two weeks
    15 GLH
    4 tasks submitted
'''

menu = """
Investment - To calculate the amount of interest you'll earn on your investment)

Bond       - To calculate the amount you'll have to pay on a home loan"
"""

while True:
    print(menu)
    selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    print(f" You have selected: {selection}!")

    # amount, years, interest rate
    if selection == "bond":
        #
        p = float(input("Enter the present value of your house: "))

        r = float(input("Enter the monthly interest rate, excluding the percentage symbol: ")) / 100
        r = r / 12

        t = int(input("Enter the number of months for the loan: "))

        calculation_selection = input("Enter either 'simple' or 'compound' interest: ").lower()

        if calculation_selection == "simple":
            print("")

        elif calculation_selection == "compound":
            print("")

        else:
            print("Don't be silly!")

    else:
        print("invalid input")