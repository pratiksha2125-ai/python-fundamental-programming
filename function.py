

# sum of two numbers
# def add(a, b):
#     return a + b

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# result = add(x, y)
# print("Addition of numbers:", result)

# check number is even or odd

# def check(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"

# n = int(input("Enter a number:"))
# result=check(n)
# print("The  number is:",result)

# Factrorial

# def factorial(n):
#     if n<0:
#         return"Factorial not defined for nagative number "
#     result=1
#     for i in range(1,n+1):
#         result *=i

#     return result
# num=int(input("Enter a number:"))
# print("Factorial:",factorial(num))

# -----------------------video--------------------------------
# def calculategmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)

# a=9
# b=8
# # gmean=(a*b)/(a+b)
# # print(gmean)
# def isGreater(a,b):
#  if(a>b):
#     print("First number is grester")
#  else:
#      print("Second number is grester or equal")

# def isLesser(a,b):
#    pass #it means the function we write a later so plese go to the next statement.

# isGreater(a,b)
# calculategmean(a,b)
# c=8
# d=7
# # if(c>d):
# #     print("First number is grester")
# # else:
# #     print("Second number is grester or equal")
# isGreater(c,d)
# calculategmean(c,d)


# def average(a=9,b=1):
#     print("The average is:",(a+b)/2)
# average() # this is default arguments
# average(1,5)


def evenodd(num):
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")
evenodd(45)