

# python using multiple methods
text="  hello\tworld python programming 123 "
# print("Original string",repr(text))
# # captitalize()
# print("\n capitalize():",text.capitalize())
# # casefold()
# print("casefold():",text.casefold())
# # center()
# print("center():",text.center(50,"*"))
# # count
# print("count('o'):",text.count('o'))
# # encode
# print("encode():",text.encode())
# # endswith()
# print("endswith():",text.endswith('123  '))
# # expandtabs()
# print("Expandtabs()",text.expandtabs(4))
# # find
# print("find():",text.find("python"))
# # format()
# name="pratiksha"
# print("format():my name is {}".format(name))
# # format_map()
# date={"fruit":"apple","price":100}
# print("format_map():{fruit}cost{price} ruppes".format_map(date))
# # index
# print("index('world'):",text.index('world'))
# # isalnum()
# print("abc123:","abc123".isalnum())
# # isalpha()
# print("python.isalpha():","python".isalpha())
# # isdecimal()
# print("456.isdigit:","123".isdecimal())
# # isdigit
# print("456 :","456".isdigit())
# # isidentifier
# print("my_var :","my_var".isidentifier())
# # islower()
# print("lowercase:","hello".islower())
# # isnumeric
# print("789".isnumeric())
# # isprintable
# print("789".isprintable())
# # isspace()
# print("  ".isspace())
# # istitle()
# print("Hello World".istitle())
# # isupper()
# print("HELLO".isupper())
# # join
# word=["python","is","easy"]
# print("join():".join(word))
# # ljust
# print("ljust:","python".ljust(15,"-"))
# # lower
# print("HELLO".lower())
# # lstrip()
# print(text.lstrip())


# maketras() and traslate()
# trans=str.maketrans("aeiou","12345")
# print("education".translate(trans))
# # partition
# print(text.partition("world"))
# # replace()
# print(text.replace("pyhton","java"))

# # rfind
# print(text.rfind("o"))
# # rindex
# print(text.rindex("o"))
# # rjust
# print("pyhton".rjust(15,"-"))
# # rpartition()
# print(text.rpartition("python"))
# # rsplit()
# print(text.rsplit(" ",2))
# # rstrip()
# print(text.rstrip())

# # splitlines()
# # multi="Hello\nworld\npythpn"
# # print(multi.splitlines())

# # # startwith()
# # print(text.startswith("  hello"))

# # # strip()
# # print(text.strip())
# # swapcase()
# print("pyThOn".swapcase())
# # title()
# print("welcome to python".title())
# # upper()
# print("python".upper())
# # zfill()
# print("25".zfill(5))


str=input("Enter a string:")
if(str==str[::-1]):
    print("String is palindrom")
else:
    print("String is not palindrom")