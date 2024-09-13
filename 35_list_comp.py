items = [1,2,3,4,5,6,7,8,10]

# list_2 = []
# for item in items:
#     if item%2 == 0:
#         list_2.append(item)
# print("using with list comphreh",list_2)


# list_2 = [item for item in items if item%2==0]
# print("using list comprhension",list_2)

#class work, square of each item in list
items = [1,2,3,4,5,6,7,8,10] 
        # [1,4,9,16.........]

# new_list = []
# for item in items:
#     new_list.append(item*item*item)


# print(new_list)

new_list = [item*item for item in items]
print(new_list)


# WAP to store list item by adding 1000 in new list


for i in items: 
    if i%2 ==  0:
        print("it is even number")
    else:
        print("it is odd number")