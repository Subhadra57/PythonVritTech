#Write a program to add item in tuple

first_tuple = ("mathematics","python","c++")
print(type(first_tuple))
list_data = list(first_tuple)
print(type(list_data))
list_data.append("980")
print(list_data)
first_tuple = tuple(list_data)
print(first_tuple)