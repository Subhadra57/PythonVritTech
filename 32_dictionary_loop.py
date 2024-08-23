subject = {
    "math":54,
    "science":78,
    "nepali":98,
    "english": 90
}

# print(subject["science"])

for key in subject.keys():
    print(f"your mark in {key} subject is {subject[key]}")


#WAP to ask subject and their mark and print their percentage and division

for i in range(1,6):
    subject = input("Enter the subject name: ")
    mark = int(input("Enter the mark: "))