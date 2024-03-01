'''
start
Variable assignment, qualifying time for each competition
    ask for input for these races
    assign a variable to the total time taken for the competition by using addition opperators
        print(variable)
Assign input to award with greater than/ less than operators
    If/ elif used to assign input range
        print statement w/ f-string and explaining sentence
end
'''

# Input times for swimming, running, and cycling competitions
swimming_minutes = int(input("Enter your time in the swimming competition, in minutes: "))
running_minutes = int(input("Enter your time in the running competition, in minutes: "))
cycling_minutes = int(input("Enter your time in the cycling competition, in minutes: "))

# Calculate total time
total_time = swimming_minutes + running_minutes + cycling_minutes

# Determine the provinical award based on total time, first if statement
if total_time <= 100:
    print(f"Congratulations! Your total competition time is {total_time} minutes. You have been awarded provincial colors!")

# Determine the provinical half award based on total time, elif statement
elif 101 <= total_time <= 105:
    print(f"Well done! Your total competition time is {total_time} minutes. You have been awarded provincial half colors!")

# Determine the provinical scroll based on total time, elif statement
elif 106 <= total_time <= 110:
    print(f"Well done! Your total competition time is {total_time} minutes. You have been awarded a provincial scroll!")

# Determines no award based on total time using final else statement
else:
    print(f"You should be proud of yourself. Your total competition time is {total_time} minutes. Try again next time.")

