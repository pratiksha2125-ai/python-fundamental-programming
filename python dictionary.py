
# create and dispaly dictionary

student={
    "name":"Pratiksha",
    "roll No":3,
    "course":"Computer Diploma",
    "age":18,
    "enrollment no.":24218060176 
}
# print(student)

# Access dictionary element

# print("Name:",student["name"], "\nAge:",student["age"],"\nRoll no.",student["roll No"],"\nEnrollment ",student["enrollment no."],"\nCourse :",student["course"])
# print("Age:",student["age"


# Add new element
student["City"]="Pune"
student["Surname"]="Pasarge"
# print(student)

# Update
student["age"]="19"
# print(student)
# delete element in dictionary
del student["Surname"]
# print(student)

# check key is exit or not

# search=input("Enter value to search:")

# if search in student:
#     print("the value is present in dictionary")
# else:
#     print("the value is not exit")
# Enter value to search:name
# the value is present in dictionary