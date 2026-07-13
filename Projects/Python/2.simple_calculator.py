# Build a calculator that asks the user to enter  two  nummbers and an operator, then prints the result

#take two numbers from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# take an operator from user
operator = input("Enter an operator (+, -, *, /): ")    

# perform the calculation based on the operator
if operator == "+":
    print(num1 + num2)
elif operator=="-":
    print(num1 - num2)
elif operator=="*":
    print(num1 * num2)
elif operator=="/":
    print(num1 / num2)
else:
    print("Invalid operator. Please use +, -, *, or /.")