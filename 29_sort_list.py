first_list =[5, 1, 1, 9, 23, 54]
# first_list.sort()
# print(first_list)


temp = 5
sort_list = [] #[5]
for number in first_list:
    if number > temp:
        sort_list.append(number)
        temp = number
    else:
        sort_list.insert(len(sort_list)-1,number)
  
print(sort_list)


# assignment to short given list [1,5,9,6,89,1203,4,23]
 
# Given list
numbers = [1, 5, 9, 6, 89, 1203, 4, 23]

# Sorting the list in ascending order
numbers.sort()

# Display the sorted list
print("Sorted list:", numbers)



