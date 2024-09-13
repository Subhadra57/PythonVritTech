data = ["apple","ball","cat","dog","ball","cat"]
#WAP to remove duplicate item from list data.
# letters =  "abcdefgh"
# if 'b' in letters:
#     print("b is exists")

# algorithm

# step-1: start 
# step-2: create new_list
# step -3: loop in list data 
# step 4 :if iterable loop item exists in new_list then do nothing else append item to new list 
# step 5: print new_list 
# step 6: end


data = ["apple","ball","cat","dog","ball","cat"]
new_list = []
for item in data:
    if item in new_list:
        pass
    else:
        new_list.append(item)

print(new_list)
