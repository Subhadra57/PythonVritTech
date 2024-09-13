#WAP to make a calculator

def add(first_number,second_number):
    print(first_number + second_number) 

def subtract(first_number,second_number):
    print(first_number - second_number)

def multiply(first_number,second_number):
    print(first_number * second_number)

first_number = int(input("Enter first number#>>>... "))
operator = input("Enter operator#>>>...")
second_number = int(input("Enter second number>>>... "))

if operator == '+':
    add(first_number,second_number)
elif operator == '-':
    subtract(first_number,second_number)
elif operator == '*':
    multiply(first_number,second_number)