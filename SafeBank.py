'''
Banking app w/ a solid UI
Checking balance
Transferring funds
Depositing Money
Withdrawing money
Checking Account Limits
Confirmation prompt

Improvement 1: Implementing a Function for Pin Confirmation
Improvement 2: Adding Error Handling for Non-Numeric Inputs in Choices
'''

import random as rd

def check_bal():
    current_balance = rd.randint(100, 999999)
    return current_balance

def check_acc():
    account_check = rd.randint(1000, 99999)
    return account_check

def withdraw_balance(balance, amount):
    if amount <= balance:
        balance -= amount
        return balance
    else:
        print("Insufficient balance.")
        return balance

def confirm_pin(user_pin):
    confirm_pin = input("Enter pin to confirm: ")
    if user_pin == confirm_pin:
        print("Pin confirmed!")
        return True
    else:
        print("Incorrect pin")
        return False

print("Welcome to SafeBank Banking App!\nPlease enter your details below:")

while True:
    user_email = input("Enter your email address: ")

    if '@' in user_email and '.' in user_email:
        print("Email Exists")
    else:
        print("Invalid Email")
        continue

    user_pin = input("Enter your pin (4 digits): ")

    if len(user_pin) == 4 and user_pin.isdigit():
        print("User pin valid.")
        break
    else:
        print("Invalid pin, please try again.")

print("Welcome! Enter one of the options below:")

while True:
    print("""
    1. To check your current balance
    2. To transfer balance amount between accounts
    3. To deposit balance amount
    4. To check my account limits
    5. Withdraw balance amount
    6. Exit
    """) 
    choice = input("Enter your selection (enter the number): ")

    if not choice.isdigit():
        print("Invalid choice. Please enter a number.")
        continue

    if choice == '1':
        if confirm_pin(user_pin):
            balance = check_bal()
            print(f"Your current balance is £{balance}")

    elif choice == '2':
        if confirm_pin(user_pin):
            print("Pin confirmed!")
            transfer_amount = int(input("How much would you like to transfer: "))

            if transfer_amount > 0:
                # Implement logic to perform the transfer here
                print(f"The amount transferred is £{transfer_amount}.")
            else:
                print("Invalid amount entered, please try again!")

    elif choice == '3':
        if confirm_pin(user_pin):
            print("Pin confirmed!")
            deposit_amount = int(input("How much would you like to deposit: "))

            if deposit_amount > 0:
                # Implement logic to perform the deposit here
                print(f"The amount deposited is £{deposit_amount}.")
            else:
                print("Invalid amount entered, please try again!")

    elif choice == '4':
        if confirm_pin(user_pin):
            print("Pin confirmed!")
            account_limit = check_acc()
            print(f"Your upper limit is £{account_limit}")

    elif choice == '5':
        if confirm_pin(user_pin):
            print("Pin confirmed!")
            balance = check_bal()
            print(f"Your current balance is £{balance}")

            withdraw_amount = int(input("How much would you like to withdraw: "))

            if withdraw_amount > 0:
                balance = withdraw_balance(balance, withdraw_amount)
                print(f"You withdrew £{withdraw_amount}. Your new balance is £{balance}")
            else:
                print("Invalid amount entered, please try again!")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

# I have already changed the document