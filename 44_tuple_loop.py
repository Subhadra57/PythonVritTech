first_tuple = ("mathema","python","c++") 
# ("mathematics","pythontics","c++tics") output

#access tuple item using loop and then concat to item and at last add modified item to list , convert to tuple
modified_list = []
for item in first_tuple:
    modify_data = item+"tics"
    modified_list.append(modify_data)

modify_tuple= tuple(modified_list)
print(modify_tuple)