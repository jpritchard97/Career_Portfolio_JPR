'''
Start
Assign the variable for task given
    Assign similar but easily recognisable
Use .replace() w/ both "!" & " "
    print assigned variable
Assign new variable
Add .upper to assigned variable
    print assigned variable
Assign the idx variable 
Use [::-1] to reverse the string, i.e., [start:end:step]
    print(idx)
End
'''

# assign variable
sentence_string = "The!quick!brown!fox!jumps!over!the!lazy!dog"

# remove ! and space with .replace()
sentence_replace = sentence_string.replace("!", " ")
print(sentence_replace)

#capitalise all letters in string w/ .upper()
sentence_upper = sentence_replace.upper()
print(sentence_upper)

# Reverse string, leave start and end (without space but seperated), reverse with -1
idx = sentence_replace[::-1] # [start:end:step]
print(idx)