def convert_to_int(firs_arg):
    int_data = int(firs_arg)
    return int_data

def is_odd_even(value):
    if value % 2 == 0:
        return True
    else:
        return False

input_number = input("Enter number #>>>...")
hold_output = convert_to_int(input_number)
is_odd_even_output = is_odd_even(hold_output)
if is_odd_even_output == True:
    print(" it is even ")
else:
    print("it is odd")
