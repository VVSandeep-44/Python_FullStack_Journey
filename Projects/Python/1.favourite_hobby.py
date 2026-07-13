# a simple program that asks for user name, age and favourite hobby, then prints a fun personalized message

name = input(" What is your name? ")
age = int(input(" How old are you? "))
hobby = input(" What is your favourite hobby? ")

#print a personalized message
print(f"Hello, {name}! You are {age} years old and your favourite hobby is {hobby}. That's awesome!")