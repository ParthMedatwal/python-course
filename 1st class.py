#                                       *** PLEASE REFFER NOTES ALSO ***


print("Hello World")  #Print is a fuction that is used to display output of things written inside the bracket.
                      #here print('Hello world') will give output as = Hello World.

print('my name is Parth Sarrthi Medatwal')  # here we will get the output as = my name is Parth Sarrthi Medatwal.
                                            # Whenever we write a sentence we have to use ''or"" because sentences are "strings" which need commas to get written as output.


print('I am Parth.','my age is 22')      # In python if we want output of 2 or more strings in a single line then we seperate the strings with (,).
                                         # Here we will get output as = I am Parth. My age is 22.

print(13)       # We can also use print to write numbers.
                # here we will get output as = 13

print(13 + 12 , 10-5 , 2*11 , 4/2)     # By using print cmd we can also do addition, subtraction, multiplication, divison.
                                       # Here we will get output as = 25 5 22 2.0


print('------------------------------------------------------------------------------------------------------')
print('abc')
#*************  VARIABLES **************#

#  In python variable are locations that are assigned inside the memory of the computer.
#  Variable are names that are given to a set of values. It can be anything but has some rules of defining.
#  example of variable name are: age , name , price , size etc.
#  Variable are used to save some informative values in defined location in the memory. It can be recalled.
#  The value stored in a variable name can be changed multiple times if needed. 
#  By doing so we just change the value stored but, not the location of variable name in memory.
#  To recall a value stored in a variable name we just write print(variable name), this cmd give us the value of variablr stored in it.


# SOME EXAMPLES:

name = "parth"              # Here the variable name is 'name' & value stored is 'parth'
age = 22                    # Here the variable name is 'age' & value stored is '22'
price = 10000000000.00      # Here the variable name is 'price' & value stored is '10000000000.00'

print(name)    # this will give output as: parth
print(age)     # this will give output as: 22
print(price)   # this will give output as: 10000000000.00


# Whenever we want to recall a value of a varaible name we just write print(varaible name). 
# If we use print('variable name') we will get output as: variable name.  Because we only use ''/"" to write strings.
# example :

print("name")   # this will give output as: name ,but Not parth.


# While using variables we can get creative like:

print('My name is:', name)    # We get output as = My name is: parth
print('my age is:', age)      # We get output as = My age is: 22



# In variable we can store a variable name(location) to another variable name(location). 
# So, when we call new variable name we will get the same value stored in old variable name.
# example:

age2 = age
print(age2)   # We will get output as: 22



print('------------------------------------------------------------------------------------------------------')
print('')
#***************** DATA TYPES *****************#

# In python everything has a data type. The data type defines its nature inside python programming.
# The main data type that we focus on are: Str , int , float , bool , none.
# Here , str: String , int: Integer , Float: Decimal numbers , bool: Boolean , none: None type.
# str : sentences , int: numbers (+ve,-ve,zero) , float: decimal numbers , bool: True/false , none: unassigned variable.
# examples:


name = "Parth"
age = 22
salary = +10000000.00
a = ()
ans = False

print(type(name))     # We will get output as: str
print(type(age))      # We will get output as: int
print(type(salary))   # We will get output as: float
print(type(ans))      # We will get output as: bool


print('------------------------------------------------------------------------------------------------------')
print('')
#***************** KEYWORDS *****************#

# Keywords are words that has a predefined meaning in python. 
# These words are case sensetive i.e.. A and a are not same.
# These words cannot be used as 'indentifiers'.
# Identifiers are the words through which we can name our variable and has some rules for doing it.
# example of Keyword are: True , False , if , return , None etc.

#***************** BASIC CODES *****************#
# SUM:
a = 5
b = 5
sum = a + b
print(sum)

print()

# Diff:
a = 10
b = 5
diff = a - b
print(diff)

print('------------------------------------------------------------------------------------------------------')
print('')

#***************** OPERATORS *****************#

# In python operators are symbols that are used to perform mathematical operations between operands
# for, a + b , a & b are operands and + is an operator
# there are several operators in python some of them are: 
# Arithmetic operators , 
# Relational operators , 
# Assignment Operators , 
# logical operators

# Arithmetic Operators
a = 5
b = 2

print(a + b)  # result: 7
print(a - b)  # result: 3
print(a * b)  # result: 10
print(a / b)  # result: 2.5
print(a % b)  # % is known as modulo operator which gives remainder, so result: 1 
print(a ** b) # ** is known as power operator which give a^b, so result: 25

print()
# Relational Operators
# Relational operators are used to find some relation btw variable, further will be used in conditional statements
# it gives us result in boolean format i.e.. True or False
a = 50
b = 20

print(a == b)   # a is EQUAL TO b, Result: False
print(a != b)   # a is NOT EQUAL TO b, Result: True
print(a > b)    # a is GREATER THAN b, Result: True
print(a < b)    # a is SMALLER THAN b, Result: False
print(a >= b)   # a is GREATER THAN EQUAL TO b, Result: True
print(a <= b)   # a is SMALLER THAN EQUAL TO b, Result: False

print()
# Assignment operators
# assignment operators are used to assign a value to a variable and than perform tasks on it
num = 10
num += 10  # num = num + 10, Result: 20
print('num1:', num)     #Now, the value of num will be upadted after every opeartion and next will be performed accordingly 

num -= 10  # num = num - 10, Result: 10
print('num2:', num)

num *= 2   # num = num * 2, Result: 20
print('num3:', num)

num /= 2   # num = num / 2, Result: 10.0
print('num4:', num)

num %= 5   # num = num % 5, Result: 0
print('num5:', num)

num **= 2  # num = num ** 2, Result: 0
print('num6:', num)


# Logical operator
# there are 3 types of logical operators: not , and , or.
# they give answer in terms of boolean expressions i.e.. True or False.
# not : it calculates '==' and will give opposite value of the answer i.e.. True => False and False => True.
# and: it will give result as True if both statements are True, else Flase and also False if both are False.
# or: it will give result as True if anyone of the two values are True, and Flase if both values are False. 
a = 5
b = 2

print("not operator:", not (a > b))                 # result: False i.e.. opposite of True
print("not operator:", not (b > a))                 # result: True i.e.. opposite of False
print("and operator:", (a != b ) and (b != a))      # result: True , cuz both are true
print("and operator:", (a == b ) and (b == a))      # result: False, cuz both are False
print("and operator:", (a != b ) and (b == a))      # result: False, cuz both are different
print("or operator:", (a != b) or (b == a))         # result: True, cuz one of them is True
print("or operator:", (a == b) or (b == a))         # result: False, cuz both are False


print('------------------------------------------------------------------------------------------------------')
print('')
#***************** TYPE CONVERSION *****************#
# in python type conversion is used to change the class type of the variable.
# Basically, the conversion is of two type: type conversion(done automaticaly) and type casting(done manually)
# Type Coversion:
a = 2           # Class type = int
b = 4.25        # Class type = float
sum = a + b
print(a + b)    # Result: 6.25, answer will be converted to superier class

print()

# Type Casting
a = "2"         # Class type = str
b = 4.25        # Class type = float

c = float(a)    # Type casting done, Can also be done for different type.

sum = c + b     # Class type = float
print(sum)      # Result: 6.25 

# A string can not be added to a int or float because character cannot be added to numbers. But a string can be added to string
# example: a = "Parth", b = 2 ; sum = a + b (cannot be done gives error)
# example: a = "Parth", b = "Medatwal" ; sum = a + b => ParthMedatwal 

print('------------------------------------------------------------------------------------------------------')
print('')
#***************** INPUTS IN PYTHON *****************#
# In python we can also take input from the user at time of code excution.
# To do so we use function named 'input()'. By default any value entered in the input() is a String value.
# To change the class of the input() at desired times we can use int(input()) and float(input()), this will give class as int and float respectively.
# examples:
age = input("enter your age:")
print(type(age))         # gives class as: str

print()

age = int(input("enter your age:"))
print(type(age))        # gives class as: int

print()

marks = float(input("enter your marks:"))
print(type(marks))      # gives class as: float



print('------------------------------------------------------------------------------------------------------')
print('')
#***************** Practice questions *****************#

# QUESTION 1: Take two numbers from user and perform sum.
a = int(input("enter your 1st number:"))
print(type(a))

print()

b = float(input("enter your 2nd number:"))
print(type(b))

print()

sum = a + b
print("Sum of your two numbers is:", sum)
print(type(sum))

print('------------------------------------------------------------------------------------------------------')
print()

# QUESTION 2: Take input for sides of square and find its perimeter and area
a = int(input("enter the value for one side of square:"))

perimeter = a * 4
print("the perimeter of your square is:", perimeter)

area = a ** 2
print("the area of your square is:", area)

print('------------------------------------------------------------------------------------------------------')
print('')
# QUESTION 3: Take two floating point numbers and do their average
a = float(input("enter 1st number:"))
b = float(input("enter 2nd number:"))

avg = (a + b) / 2

print("the average is:", avg)
print(type(avg))

print('------------------------------------------------------------------------------------------------------')
print('')
# QUESTION 4: Take value for a and b. Then print True if a is greater than b and False if not.
a = float(input("enter value for a:"))
b = float(input("enter value for b:"))

ans = not(a < b)
print(ans)