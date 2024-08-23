#WAP to ask subject and their mark and print their percentage and division
# output should be like 
# {'math': 55, 'english': 63, 'nepali': 45, 'percentage': 55, 'division': 'second division'}
# for i in range(1,6):
#     subject = input("Enter the subject name: ")
#     mark = int(input("Enter the mark: "))
total_student_list = []
for student in range(0,3):
    subject_mark = {}
    obtain_mark = 0
    student_name = input("Enter student name: ")
    for i in range(1,4):
        subject = input("Enter the subject name: ")
        mark = input("Enter the mark: ")
        subject_mark[subject] = mark
        obtain_mark = obtain_mark + int(mark)
    percentage = (obtain_mark/500)*100
    percentage = percentage
    if percentage < 30:
        division = "fail"
    elif percentage>=30 and percentage<45:
        division = "third division"
    elif percentage>=45:
        division = "second division"
    else:
        division = "first division"
    subject_mark['percentage']=percentage
    subject_mark["division"] = division
    subject_mark['student_name'] = student_name
    total_student_list.append(subject_mark)
print("**********************total studen data***********************")
print(total_student_list)
# [{'student_name':"ram",'nepali':66,'english':43},{'student_name':"hari",'nepali':66,'english':43}]
# [{'student_name':"ram",'nepali':66,'english':43},{'student_name':"hari",'nepali':66,'english':43}]
