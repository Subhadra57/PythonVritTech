#WAP to make a calculator ,and choices is like y/n if , user press "y" then he can add,susbtract,
        #if user input 'n' then terminate calculating process.

#WAP to take 5 input number from user and find sum of all number


total_sum = 0

for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    total_sum += number

print("The sum of the numbers is:", total_sum)

























# while True:
#     first_number = int(input("Enter first number#>>>"))
#     secocnd_number = int(input("Enter Second number#>>>"))
#     operator = input("Enter operator number#>>>")

#     if operator == '+':
#         print(first_number+secocnd_number)
#     elif operator == '-':
#         print(first_number-secocnd_number)
#     elif operator == '*':
#         print(first_number*secocnd_number)
    
#     is_play  = input("Do you want to play again ? 'y/n'#>>> ")
#     if is_play == 'n':
#         break























# def calculator():
#     while True:
#         print("Welcome to the calculator!")
#         choice = input("Do you want to perform an operation? (y/n): ")

#         if choice.lower() == 'y':
#             print("Choose an operation:")
#             print("1. Addition")
#             print("2. Subtraction")

#             operation = input("Enter 1 for addition or 2 for subtraction: ")

#             if operation == '1':
#                 num1 = float(input("Enter the first number: "))
#                 num2 = float(input("Enter the second number: "))
#                 result = num1 + num2
#                 print(f"The result of {num1} + {num2} is {result}")

#             elif operation == '2':
#                 num1 = float(input("Enter the first number: "))
#                 num2 = float(input("Enter the second number: "))
#                 result = num1 - num2
#                 print(f"The result of {num1} - {num2} is {result}")

#             else:
#                 print("Invalid operation. Please choose either 1 or 2.")

#         elif choice.lower() == 'n':
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter 'y' or 'n'.")

# # Run the calculator function
# calculator()




