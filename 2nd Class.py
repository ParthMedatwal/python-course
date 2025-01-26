#                                       PLEASE REFFER NOTES ALSO


#*************** STRINGS *****************#

# Strings can we written by using: ' ' or " " or """ """
# Every appostrofy have its significance in python. 
# example: 
# 'this is parth's python codes' : this is not valid cuz python only knows to count from 1st appostrofy type to 2nd. Here python will only count string till 's.
# To solve the above problem we use different way to demonstrate it : " this is parth's python code " : this whole sentence is valid now as a single string.

str1 = 'Parth'
str2 = "Parth"
str3 = """Parth"""
print(str1)
print(str2)
print(str3)

print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** BASIC STRINGS OPERATIONS *****************#

# Concatination: means adding two or more strings
str1 = 'Parth'
str2 = 'Medatwal'
str3 = str1 + str2
print(str1 + str2)
print(str3)


# len() : this counts the number of characters, numbers, special characters, spaces etc. in a string.
str1 = 'Parth'
len1 = len(str1)

str2 = 'Medatwal'
len2 = len(str2)

str3 = str1 + "" + str2
len3 = len(str3)

print(len1)
print(len2)
print(len3)


print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** INDEXING *****************#
# In Python every element of a string has its unique position number, which signifies its location inside a string.
# example: "PARTH 123"
#           012345678
# We can print a specific character of a string by recalling it with 'str[index number]'

str = "PARTH 123"

print(str[4])
print(str[5])
print(str[7]) 

# In indexing we cannot change or reassign a element of a string by using str[]
# example: str[5] = @     : this is invalid cuz not allowed in Python


print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** SLICING *****************#
# Slicing is used in python to print some specific charatcers of a string
# It can be done using str[starting indx : ending indx]
# Here, the starting index number is included in output, but the ending index number is not included
# Slicing is heavily used in Machine Learning algorithms
# example: 

str = 'Parth'
#      01234

print(str[1 : 4])           # Result: art
print(str[1 : 5])           # Result: arth
print(str[0 : 5])           # Result: Parth
print(str[0 : len(str)])    # Result: Parth, len(str) means counting till last character of the string.

# str[ : 5] = str[0 : 5] , Python will consider it as this
# str[1 : ] = str[1 : len(str)] , Python will consider it as this


print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** -VE INDEXED SLICING *****************#
# In python we can also give string a =ve index.
# It can be done using str[starting indx : ending indx]
# Here, the starting index number is included in output, but the ending index number is not included
# example: 'P  a  r  t  h'          , Gap is only given to understand things
#          -5 -4 -3 -2 -1               

str = 'Parth'

print(str[-3 : -1])         # Result: rt
print(str[-5 : len(str)])   # Result: Parth
print(str[ : len(str)])     # Result: Parth
print(str[-5 : ])           # Result: Parth


print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** STRING OPERATIONS *****************#
# there are many operations that we can use on strings in python. Few of them are:

str = "i am Parth a current student of university of waterloo"

# str.endswith() this will give output as True/False is the end character is same or different from which is passed inside this function.
print(str.endswith('loo'))
print(str.endswith('rth'))

# str.capitalize() this will capitalize the 1st character of the string
print(str.capitalize())

# str.replace(old,new) this will replace the old value with a new inside a string
print(str.replace("Parth","Yash")) 

# str.find() this will give the index value of the word or a character that occurs for the 1st time inside the string
print(str.find("waterloo"))
print(str.find("a"))

# str.count() this counts the number of times the word or character is repeated inside the string
print(str.count("a"))



print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** PRACTICE QUESTIONS *****************#

# QUESTION 1: WAP TO INPUT USER NAME AND COUNT ITS LENGTH
name = input("what is your name?:")
print("Hello", name)
print("The lenght of your name is:",len(name))

print('--------------------------------------------------------------------------------------------------------------')
print()
# QUESTION 2: WAP TO FIND THE OCCURANCE OF '$' IN A STRING
str = input("write anything with dollar sign inculded:")
print("You have entered:", str)
print("The dollar sign has occured these many times:", str.count("$"))



print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** CONDITIONAL STATEMENTS *****************#
# There are 3 major conditional statements in Python i.e.. if , elif and else
# if: This is a condition that is always written at the top and the code will always test it 1st if it is written in code.
#     We can use it multiple times to make our code run.

# elif: This is a short form of (else if), this is always executed after an if condition and cannot be used as the starting condition.
#       hence, it always requires an if statement above it.
#       We can use it multiple times in code after one if statement at the starting of the code.

# else: This is a conditional statement that is used only once in a code and at the last. 
#       We use it to define the last condition to be true in a code.
#       It always requires an if statement before it. 
#       We cannot use it multiple times inside a code.

# Example:
age = int(input("what is your age?:"))

if(age >= 18):
    print("You are eligible to vote !!")

elif(age >= 21):
    print("You are eligible to vote & to get married !!")

else:
    print("You are small in age !!")

print("End of code")


print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** PRACTICE QUESTIONS *****************#

# QUESTION 1: WAP TO GRADE STUDENTS ACCORDING TO THEIR MARKS

marks = float(input("Enter your marks:"))

if(marks > 90):
    print("Grade A")

elif(90 > marks >= 80):
    print("Grade B")

elif(80 > marks >= 70):
    print("Grade C")

elif(70 > marks >= 60):
    print("Grade D")

else:
    print("Low Grades test Failed!!")

print("end of report")


print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** NESTING *****************#
# Nesting means using confitions inside a predefined condition
# example:

age = 35

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")

else:
    print("cannot drive")


print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** PRACTICE QUESTIONS *****************#

# QUESTION 1: WAP TO CHECK IF THE NUMBER BY USER IS ODD OR EVEN
num = float(input("Enter a number:"))

if(num % 2 == 0):
    print("Even")

else:
    print("Odd")

print('--------------------------------------------------------------------------------------------------------------')
print()

# QUESTION 2: WAP TO FIND GREATEST AMONG 3 NUMBER ENTERED BY USER
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if(a > b and a >= c):
    print("greatest number is:", a)
    
elif(b > c):
    print("greatest number is:", b)

else:
    print("greatest number is:", c)

print("end of code")


print('--------------------------------------------------------------------------------------------------------------')
print()

# QUESTION 3: WAP TO CHECK IS THE NUMBER FROM USER IS MULTIPLE OF 7 OR NOT
num = int(input("Enter a number of your chocie:"))

if(num % 7 == 0):
    print("It is a multiple of 7")

else:
    print("Not a multiple of 7")