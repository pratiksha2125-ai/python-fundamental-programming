


# 🟢 Beginner Level Solutions
# 1. Print numbers 1 to 10

# for i in range(1,11):
#     print(i)

# print even numbers 1 to 20
# for i in range (1,21):
#     if(i%2==0):
#         print(i)

#print the sum of first nth numbers
# n =int(input("Enter a number:"))
# sum= 0
# for i in range(1, n + 1):
#     sum=sum+i
# print(sum)

# print multiplication tabel

# n=int(input("Enter a number:"))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

# count the number of digit in number 

# n=int(input("Enter a number:"))
# count=0
# while n>0:
#     n//=10
#     count+=1
#     print(count)

# reverse the number
# num=int(input("Enter a number:"))
# rev=0
# while  num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num//10
#     print(rev)



# strong number :- if  number=sum of factorial of its digit then it is  called as strong number

num=int(input("Enter a number :"))
temp=num
sum_fact=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
        sum_fact=sum_fact+fact
        temp//10

print("Strong"if sum_fact==num else "Not")