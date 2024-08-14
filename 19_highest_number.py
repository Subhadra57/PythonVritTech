# data = "822457313496"

# first_number = 1
# second_number = 5

# if first_number>second_number:
#         print(first_number , "highest number")
# else:
#         print(second_number , "highest number")

# zero step : highest_number = 0
# first-step :  iterate over data 
# second-step: assign iterate value to a variable
# third-step: convert string value to intiger
# 4th-step:compare highest_number is greater or  lower than iterate number
# 5th-step : if highest_number is greater than iterate number then do nothing 
#                 else 
#             highest_number = iterate number 
# 6th step: print highest_number


data = "328741256"

highest_number = 0


for number in data:
    number = int(number)
    if number > highest_number:
        highest_number = number
    else:
        pass

print(highest_number)