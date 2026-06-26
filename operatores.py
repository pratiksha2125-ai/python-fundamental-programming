

# Advanced Arithmetic Operator Program

# print("Simple Calculator")

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("Choose operation")
# print("1.Addition")
# print("2.Subtraction")
# print("3.Multiplication")
# print("4.Division")
# print("5.Modulus")
# print("6.Power")

# choice = int(input("Enter choice: "))

# if choice == 1:
#     print("Result =", a + b)
# elif choice == 2:
#     print("Result =", a - b)
# elif choice == 3:
#     print("Result =", a * b)
# elif choice == 4:
#     print("Result =", a / b)
# elif choice == 5:
#     print("Result =", a % b)
# elif choice == 6:
#     print("Result =", a ** b)
# else:
#     print("Invalid choice")

# program of logical and relational

# marks1=int(input("Enter a marks of subject 1:"))
# marks2=int(input("Enter a marks of subject 2:"))
# marks3=int(input("Enter a marks of subject 3:"))
# marks4=int(input("Enter a marks of subject 4:"))
# marks5=int(input("Enter a marks of subject 5:"))

# total=marks1+marks2+marks3+marks4+marks5
# average=total/5

# if marks1 >=35 and marks2>=35 and marks3>=35 and marks4>=35 and marks5>=35:
#     print("Result: PASS😊😊")
# else:
#     print("\n Result:FAIL😭😭") 

# if average >=75:
#     print("\n Grade: Distriction😍😍")
# elif average>=60:
#     print("\n Grade:First class☺️☺️☺️")
# elif average>=50:
#     print("\n Grade :Second class🙂🙂🙂")
# else:
#     print("Grade:Third class😒😒")

# Bitwise operation
# a=int(input("Enter a first number:"))
# b=int(input("Enter a second number:"))

# print("Bitwise AND:",a&b)
# print("Bitwise OR:",a|b)
# print("Bitwise XOR:",a^b)
# print("Bitwise NOT  of a:",~a)
# print("left shft of a :",a<<2)
# print("Right shift a",a>>2)

# member operator program
# number=[10,20,30,40,50,60]
# num=int(input("Enter a number to search:"))

# if num in number: #this is a operator
#     print("Number is found")
# else:
#     print("Number is not found")

# identity operator program

# list1=[1,2,3,4]
# list2=[1,2,3,4]
# list3=list1

# print("list1 is list2",list1 is list2)
# print("list1 is list3",list1 is list3)
# print("list1 == list2",list1 == list2)

# Assignment Operators

a = 10

print("Initial value:", a)

a += 5
print("a += 5 :", a)

a -= 3
print("a -= 3 :", a)

a *= 2
print("a *= 2 :", a)

a /= 4
print("a /= 4 :", a)

a %= 3
print("a %= 3 :", a)