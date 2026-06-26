

# create and print list
num=[10,20,30,40,50]
print("List elements are :",num)
# add element in list
num.append(100)
num.append(200)
print("List append elements are :",num)
# remove element
num.remove(20)
print("List remove elements are :",num)
#find maximum number
# large=max(num)
print("List max elements are :",max(num))
# find min
print("List min elements are :",min(num))
# find sum
print("List sum elements are :",sum(num))
# check elemnt is present or not
n=int(input("Enter number to search:"))
if n in num:
    print("Number exit")
else:
    print("Number is not exit")
 
# print number in reverse
num.reverse()
print("List reverse order elements are :",num)

# sort list
num.sort()
print("list is sorted:",num)
# count even and odd number
num.append(35)
odd = 0
even = 0
for  i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("number of even:",even)
print("Number of odd :",odd)
# take list input from user
col=[]
c=int(input("How many elements:"))
for i in range(c):
    value=int(input("Enter number:"))
    col.append(value)
print("List is:",col)
# find duplicate elements
num.append(30)
num.append(10)
num.append(100)
dup=[]
for i in num:
    if num.count(i)>1 and i not in dup:
        dup.append(i)
print("duplicate values:",dup)
# merge two lists
merge=col+num
print("combination of two lists:",merge)
# remove duplicate values
unique=[]
for i in merge:
    if i not in unique:
        unique.append(i)
print("Removed",unique)
# second largest number
unique.sort()
print("Second largest number:",unique[-2])
# separate positive and negative number
num.append(-20)
num.append(-30)
pos=[]
neg=[]
for i in num:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)

print("Positive:",pos)
print("Negative:",neg)
# list palindrome check
# it is check whole list not every elemnt like 11,22,33
if num==num[::-1]:
    print("palindrome list")
else:
    print("Not palindrome list")
# find frequency of elements


for i in merge:
    print(i,"appears",merge.count(i),"times")
# copy list
fruit=["apple","orange","banana"]
copy_list=fruit.copy()
print("copied list",copy_list)
# square of list elemnts
square=[]
for i in merge:
    square.append(i*i)
print("Square of List Elements",square)