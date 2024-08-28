#WAP to make crud application for school 
# c=create (store)
# r = read 
# u = update
# d = delete

student_data = []

while True:
    print("************WELCOME*************************")
    print("select 1 for register new student")
    print("select 2 for display all students")
    print("select 3 for search student")
    print("select 4 for register update student")
    print("""select 5 for register delete student \n
    do you want to exit ? Y/N""")

    input_option =  input("#>>>...")

    if input_option == "1":
        name = input("enter name:")
        age = input("enter age:")
        roll = input("enter roll:")
        student = {"name": name, "age": age, "roll": roll}
        student_data.append(student)

    if input_option == "2":
        for student in student_data:
            print(student)

    if input_option == "3":
        roll = input("enter roll to search:")
        for student in student_data:
            if roll in student['roll']:
                print("congrats ! student found", student)