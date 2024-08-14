#WAP to find lowest number amongs  "822457313496"

data = "822457313496"

lowest_number = 0


for number in data:
    number = int(number)
    if number < lowest_number:
        lowest_number = number
    else:
        pass

print(lowest_number)