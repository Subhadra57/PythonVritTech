#WAP to find out a given number is prime or not
    #  where isPrime must be a function which return True and False for 
    #  determine either number is prime or composite.

input_number = 11

def is_prime(value):
    count = 0
    for i in range(1,input_number+1):
        if value%i == 0:
            count = count + 1
    if count>2:
        return False
    else:
        return True

number = int(input("Enter any number#>>>...."))
is_prime_output = is_prime(number)
if is_prime_output == True:
    print("it is prime ")
else:
    print("it is composite number")