''' Start

1. What is required to complete the task?
2. name & age as variable identifiers
3. -- use name = input("argument") 
4. ---- add .capitalize() to the name
5. -- use age = input("argument")
6. use sentence as a variable and concatenate the sentence
7.use a function with {} to clean code
8. print code

end '''

#define variable identifiers, i.e., name =, age =, street =.

name = input("pleae enter your name: ").capitalize()
age = input("please enter your age: ")
street_number = input("please enter your flat or house number: ")
street = input("please enter your street number and name: ").capitalize()


#concatenate sentence
#sentence = "This is " + name + " they are " + age + " years old... " 
#functions and spaces included

sentence = f"This is {name}, they are {age} years old, and lives at {street_number} {street}"
print(sentence)
