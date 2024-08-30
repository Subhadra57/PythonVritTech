# def addtion(a,b):
#     return int(a)+int(b)

# for i in range(4):
#     first_number = input("Enter first number#>>>...")
#     second_number = input("second number#>>>... ")
#     output = addtion(first_number,second_number)
#     print(output+50)

# class work to make calculator, make function of each operator
# def addition(a,b):
#     return int(a)+int(b)
# def subtraction(a,b):
#     return int(a)-int(b)
# def multiply(a,b):
#     return int(a)*int(b)
# def divide(a,b):
#     return int(a)/int(b)

# first_number = input("Enter first number:")
# operator = input("Enter operator:")
# second_number = input("Enter second number:")
# if operator == '+':
#     output = addition(first_number,second_number)
# elif operator =='-':
#      output = subtraction(first_number,second_number)
# elif operator =='*':
#     output = multiply(first_number,second_number)
# elif operator =='/':
#     output = divide(first_number,second_number)
# else:
#     print("Invalid operator")

#     print(output)



# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b

# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")


#     choice = input("Enter choice (1/2/3/4): ")

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == '1':
#         print(f"The result is: {add(num1, num2)}")
#     elif choice == '2':
#         print(f"The result is: {subtract(num1, num2)}")
#     elif choice == '3':
#         print(f"The result is: {multiply(num1, num2)}")
#     elif choice == '4':
#         print(f"The result is: {divide(num1, num2)}")
#     else:
#         print("Invalid input")


# calculator()


def is_prime(number):
    # Check if number is less than 2, which are not prime
    if number <= 1:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Input: A number to check
num = int(input("Enter a number: "))

# Output: Checking if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")





