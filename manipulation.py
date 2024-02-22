'''
Start
Assign variable to give input
Assign variable for symbol replacement
Find sentence length via len()
    Combine print and len() in single line
Find last letter in input sentence via indexing
Use .replace() and the assigned variable to replace last letter in input senctence with "@"
    Assign variable for print()
Assign new variable ad use indexing on original input via start:end:step
    print()
Take the first 3 letters and last 2 letters of input via slicing
    Conjugate each slice and print()
End
'''

#Ask for sentence input
str_manip = input("Enter a random sentence: ")

# Assign symbol for .replace()
symbol_replace = "@"

# Find sentence length
print(len(str_manip))

# Find lasr char of input
str_manip_last_letter = str_manip[-1]

# Use .replace() and input the previously assigned variables
# Note: Could not work out how to just use the "@" within the .replace()
str_manip_replace = str_manip.replace(str_manip_last_letter, symbol_replace)
print(str_manip_replace)

# Find last three letters and reverse them (slicing)
str_manip_reverse_chars = str_manip[-1:-4:-1]
print(str_manip_reverse_chars)

# Concatenating the sliced string together
str_manip_idx = str_manip[0:3] + str_manip[-2:-1] + str_manip[-1]
print(str_manip_idx)