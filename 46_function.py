def design():
#     print("-----------WELCOME HERE-------------------")
#     print("******************************************")

 def design_star(design_value):
    welcome = "-----------WELCOME HERE-------------------\n"
    full_design = welcome+design_value
    return full_design




def application():

    print("select 1 for register new student")
    print("select 2 for display all students")
    print("select 3 for search student")
    print("select 4 for register update student")

    user_input = input("Enter your choice#>>>...")
    if user_input == "1":
        print("user create success !!!")
    elif user_input == "2":
        print("user display !!!")


# design = design_star("***************************************")
# print(design+" custom modify")
# application()
# design = design_star("#######################################")
# print(design)
# application()

