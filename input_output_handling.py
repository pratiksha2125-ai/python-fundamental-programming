# write data into a file

# file =open("myfile.txt","w")
# file.write("Hello python\n ")
# file.write("File handling example")
# file.close()
# print("Data written to file sucesfully")

# Read text from a file
file =open ("myfile.txt","r")
data=file.read()
print(data)
file.close()

# Append data to existing file

# file=open("myfile.txt","a")
# file.write("\n this line added later.")
# file.close()
# print("Data appended successfully.")

# file =open ("myfile.txt","r")
# data=file.read()
# print(data)
# file.close()


# read file line by line 
# file=open("myfile.txt","r")
# for line in file:
#     print(line)
# file.close()

# count number of lines in file

# file=open("myfile.txt","r")
# count=0

# for line in file:
#     count+=1
# print("total lines:",count)
# file.close()

# count word in file

# file=open("myfile.txt","r")
# data=file.read()
# words=data.split()
# print("Total words:",len(words))
# file.close()

# copy contain from one file to another file
# f1=open("demo.txt","r")
# f2=open("copy.txt","w")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()
# print("File copied successfully")


# using with statement
# with open("demo.txt","r") as file:
#     data=file.read()
#     print(data)


# write list of lines to files

# lines=["python\n","java\n","c++\n"]

# # with open("languages.txt","w") as f1:
#     # f2.writelines(lines)

# # print("lines written successfully.")

# word=input("Enter word to search:")
# with open("languages.txt","r") as f2:
#     data=f2.read()
#     if word in data:
#         print("word is found")
#     else:
#         print("Word is not found")


# f=open("nums.txt","w")
# for i in range(1,11):
#     f.write(str(i)+"\n")
# f1=open("nums.txt","r")
# f.close()
# print(f1.readline()) read first line 
# lines=f1.readlines() 
# print(lines[-1]) read last character
# data=f1.read()[::-1] data in reverse order
# f1.close()
# print(data)


# Write a list to file
# lis=["a\n","b\n","c\n"]
# f=open("list.txt","w")
# f.writelines(lis)
# f.close()

# remove blank lines
# f=open("data.txt","w")
# f.write("hi my name is pratiksha pasarge\n" \
# "\n now i am learning python programming \n\n for data science")
# f.close()
# f=open("data.txt","r")
# data=f.read()
# print("---------------------------------Before---------------------------------------")
# print(data)
# f.close()
# f=open("data.txt","r")
# lines=f.readlines()
# f.close()
# f=open("Clear.txt","w")
# for line in lines:
#     if line.strip() !="":
#         f.write(line)
# print("Blanks lines are remove")

# f.close()
# f=open("Clear.txt","r")
# data=f.read()
# print("---------------------------------After---------------------------------------")

# print(data)
# f.close()


# f=open("data.txt","w")
# f.write("hi my name is pratiksha pasarge\n" \
# "\n now i am learning python programming \n\n for data science")
# f.close()
# print("---------------------------------Before---------------------------------------")
# f=open("data.txt","r")
# data=f.read()
# print(data)
# f.close()

# f=open("upper.txt","w")
# f.write(data.upper())
# f.close()
# print("---------------------------------After---------------------------------------")
# f=open("upper.txt","r")
# data=f.read()
# print(data)
# f.close()

# string in lower case
# data=(open("data.txt","w"))
# data.write("HI MY NAME IS PRATIKSHA PASARGE")
# data.close()
# print("Before:\n",open("data.txt").read())
# open("lower.txt","w").write(open("data.txt").read().lower())
# print("After:\n",open("lower.txt").read())

# constant and vowels
# f=(open("data.txt","w"))
# f.write("HI MY NAME IS PRATIKSHA PASARGE")
# f.close()
# data=(open("data.txt","r").read().lower())

# vowels=set("aeiou")
# v=c=0
# for ch in data:
#     if ch.isalpha():
#         if ch in vowels:
#             v+=1
#         else:
#             c+=1
# print("Vowels:",v)
# print("Consonants:",+c)

# even and odd numbers

# f=open("number.txt","w")
# f.write(input("Enter a number:"))
# f.close()
# f=open("number.txt","r")
# num=int(f.read())
# f.close()

# if num%2==0:
#     print("The number is Even")
# else:
#     print("The number is Odd")