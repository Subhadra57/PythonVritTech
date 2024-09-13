1 # Write a Python program that asks theuser to input a number and then prints whether the number is even or odd.

# number = int(input("Please enter a number: "))
# if number % 2 == 0:
#     print(f"The number {number} is even.")
# else:
#     print(f"The number {number} is odd.")

2 # Write a program that finds the highest and lowest digit in a given string of numbers.

# number_string = input("Please enter a string of numbers: ")
# digits = [int(char) for char in number_string]

# highest_digit = max(digits)
# lowest_digit = min(digits)

# print(f"The highest digit in the string is: {highest_digit}")
# print(f"The lowest digit in the string is: {lowest_digit}")

3 # Write a program that takes a sentence as input and counts the number of words in it.

# sentence = input("Please enter a sentence: ")
# words = sentence.split()

# word_count = len(words)
# print(f"The number of words in the sentence is: {word_count}")

4 # Write a Python program that takes a positive integer as input and calculates the sum of its digits.
# number = input("Please enter a positive integer: ")

# digit_sum = sum(int(digit) for digit in number)
# print(f"The sum of the digits in {number} is: {digit_sum}")

5 # Write a program that takes a string as input and prints the string in reverse order.
# user_string = input("Please enter a string: ")
# reversed_string = user_string[::-1]

# print(f"The reversed string is: {reversed_string}")

6 #  Write a program that checks if a given word is a palindrome (reads the same forwards and backwards).

# word = input("Please enter a word: ")

# word = word.lower()

# if word == word[::-1]:
#     print(f"The word '{word}' is a palindrome.")
# else:
#     print(f"The word '{word}' is not a palindrome.")

7 # Write a program that calculates the factorial of a given number n (where n is provided by the user).

# n = int(input("Please enter a positive integer: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i
# print(f"The factorial of {n} is: {factorial}")

8 # Write a program that counts the number of vowels (a, e, i, o, u) in a given string.
# user_string = input("Please enter a string: ")

# user_string = user_string.lower()
# vowels = "aeiou"
# vowel_count = 0

# for char in user_string:
#     if char in vowels:
#         vowel_count += 1

# print(f"The number of vowels in the string is: {vowel_count}")

9 # Write a program that takes a number n as input and prints the square of all numbers from 1 to n.

# n = int(input("Please enter a positive integer: "))

# for i in range(1, n + 1):
#     square = i * i
#     print(f"The square of {i} is: {square}")

10 # Write a Python program that takes a number as input and checks whether it is positive, negative, or zero.
# number = float(input("Please enter a number: "))

# if number > 0:
#     print(f"The number {number} is positive.")
# elif number < 0:
#     print(f"The number {number} is negative.")
# else:
#     print("The number is zero.")

11 # Write a program that prints the following pattern:
# *
# **
# ***
# ****
# *****

# rows = 5

# for i in range(1, rows + 1):
#     print('*' * i)

12 # Write a Python function that takes a string as input and returns a dictionary where the keys are the words in the string, and the values are the lengths of those words.

# def word_lengths(sentence):
#     # Split the sentence into words
#     words = sentence.split()
    
#     # Create a dictionary with words as keys and their lengths as values
#     length_dict = {word: len(word) for word in words}
    
#     return length_dict

# # Example usage
# input_string = input("Please enter a sentence: ")
# result = word_lengths(input_string)
# print(result)

13 # Write a Python program that takes a list of students'
# names and their corresponding marks in a subject, stores them in a dictionary, and then calculates and prints the average mark.

# def calculate_average_marks():
#     # Create an empty dictionary to store student names and marks
#     students_marks = {}
    
#     # Number of students
#     num_students = int(input("Enter the number of students: "))
    
#     # Get student names and marks from the user
#     for _ in range(num_students):
#         name = input("Enter the student's name: ")
#         mark = float(input(f"Enter {name}'s mark: "))
#         students_marks[name] = mark
    
#     # Calculate the average mark
#     total_marks = sum(students_marks.values())
#     average_mark = total_marks / num_students
    
#     # Print the average mark
#     print(f"The average mark is: {average_mark:.2f}")

# # Call the function
# calculate_average_marks()
