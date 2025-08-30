str1 = "Hello world"
str2 = "parth"
str3 = "nedatwal"

print(str1)
print(str2)
print(str3)

print(str1 + " " + str2 + " " + str3)

print(len(str1))
print(len(str2))
print(len(str3))

print(len(str1 + " " + str2 + " " + str3))

name = "John Doe"
print(name[4])
print(name[1])

print(name[0:4])
print(name[1 :])
print(name[:4])
print(name[: len(name)])
print(name[1: :2])

print(name[-3: -1])
print(name[: -1])
print(name[-3:])
print(name[: len(name)])

str = "i am Parth a current student of university of waterloo"

print(str.endswith("waterloo"))
print(str.endswith("rth"))
print(str.startswith("i am"))
print(str.startswith("parth"))
print(str.capitalize())
print(str.replace("a", "A"))
print(str.find("w"))
print(str.count("a"))

a = input("Enter a number: ")
b = input("Enter another number: ")
c = input("Enter a third number: ")


if(a > b and a > c):
    print("The largest number is:", a)
elif(b > a and b > c):
    print("The largest number is:", b)
else:
    print("The largest number is:", c)