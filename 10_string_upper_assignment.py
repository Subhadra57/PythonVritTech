
# upper(1):
# The upper method converts a string to upper case

str = "abc"
print(str.upper())

# lower(2)
# The lower () methods converts a string to lower case

a = "SABU"
str = "def"
print(a.lower())

# strip(3):
# The strip() removes any trailing characters. 
str = "Hello !!!!"
print(str.strip("!"))

# replace(4):
# The replace() methode replaces all occurences of a string.
str = "Silver Spoon"
print(str.replace("Sp","M"))

# split(5):
# The split() method splits the given string at the specified instance and returns the seperated as list items. 
str = "Golden Bangle"
print(str.split(" "))

# capitalize(6):
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
str1 ="hello"
capstr = str.capitalize()
print(capstr)
str2 = "hello WorlD"
capstr2 = str2.capitalize()
print(capstr2)

# center(7):
# The center() method align the string to the center as per the parameters given by the users.
str = "Welcome to the Console!!!"
print(str.center(50))

# count(8):
# The count() methode returns the number of times the given value has occured within the given string

str = "Abcaaaaaaavcvcv"
countstr = str.count("a")
print(countstr)

# endswith(9):
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

str = "Welcome to the Console !!!"
print(str.endswith("!!!"))

# find(10):
# The find() method searches for the first occurence of the given value and returns the index where it is present.if given value is absent from the string then return-1.

str = "he's name is ram. He is an honest man."
print(str.find("is"))

# replace(most imp string):
data = "i love veg food"
changed_data = data.replace('veg','non veg')
print(changed_data)

# split();
user_email = "mohan@gmail.com"
 split_data_first = user_email.split('@')
print(split_data_first)
