#                                       PLEASE REFFER NOTES


#*************** LIST IN PYTHON *****************# 
# In python when we need to store multiple values in one varialbe then we use LIST.
# It is similar to an array in C programming.
# A LIST can be represented by list = [ , , , , , ]
# Every element has a unique index and we can use the concept of indexing in LIST.
# example:

marks = [87.5  , 99 , 78 , 80 , 85]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])

print('-----------------------------------------------------------------------------------------------------------')

# we can store different datatype values in one list
# example:
data = [85 , "karan" , 12.2]
print(data)

print('-----------------------------------------------------------------------------------------------------------')

# In python list are Mutable and strings are Immutable i.e.. Mutable means elements can be changed & Immutable means elements cannot be changed if assigned one time.
# example:
str = "Parth"
print(str[0])
#str[0] = "M"   --> This cannot be done it is not allowed

list = ["Parth" , 22 , 'Canada']
print(list[0])

list[0] = "Medatwal"
print(list)

print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** SLICING *****************#
# Every rule , method and tricks of performing slicing is valid in LIST.

print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** LIST OPERATIONS *****************#
# like string, we also have some special operations with LIST.
# some of them are:

# list.append()     --> It will add a value after the last index of a list element
list = [0 , 1 , 2 , 3]
print(list)

list.append(4)
print(list)

print()

# list.sort()       --> This will sort the elements of a list in ascending order
list = [0 , 2 , 1 , 3]
print(list)

list.sort()
print(list)

print()

# list.sort(reverse=true)     --> This will sort the elements of the list in decending order
list = [0 , 2 , 1 , 3]
print(list)

list.sort(reverse=True)
print(list)

print()

# list.reverse()       --> This will reverse the element of the list without performing sorting
list = [0 , 2 , 1 , 3]
print(list)

list.reverse()
print(list)

print()

# list.insert(idx , value)      --> This will add a new value in a list at a given index, without changing the entire list
list = [0 , 2 , 1 , 3]
print(list)

list.insert(2 , "Parth")
print(list)

print()

# list.remove(element)     --> This removes the first occurance of an element in a list
list = [0 , 2 , 1 , 3 , 1 , 1]
print(list)

list.remove(1)
print(list)

print()

# list.pop(idx)        --> This will remove the element of a given index
list = [0 , 2 , 1 , 3]
print(list)

list.pop(2)
print(list)

print()  

print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** TUPLE IN PYTHON *****************#
# Tuple are same as list but they are immutable i.e.. we cannot change a value if once created just like strings
# Tuple are represented as: (value , value , value , .....)
# The values can be: str , int , float etc.
# A single value tuple is written as: (1,) or ("hello",) etc. i.e.. it is necessary to add a "," at last to consider it as tuple
# For a multiple value tuple it is optional and not necessary to add "," after last value.
# example:
tup = (1 , 2 , 3 , 4)
print(tup)
print(type(tup))

# Indexing and Slicing works as same in Tuple also

tup = (1 , 2 , 3 , 4)
print(tup[1 : 3])
print(tup[ : 2])
print(tup[ : len(tup)])

print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** TUPLE OPERATIONS *****************#

# tuple.index(value)     --> This give the index number on which the element entered is present
tup = (1, 2, 3, 4)
print(tup.index(3))       # Result: 2 (index value)

# tuple.count(value)     --> This will count the number of times the element is present in the tuple
tup = (1, 2, 3, 4, 3, 3)
print(tup.count(3))       # Result: 3 (present 3 times)

print('--------------------------------------------------------------------------------------------------------------')
print()

#*************** PRACTICE QUESTIONS *****************#

# QUESTION 1: ASK A USER TO ENTER 3 NAMES AND STORE IT IN A LIST

name = []   # for 2nd method

a = input(("Enter the 1st name:"))
b = input(("Enter the 2nd name:"))
c = input(("Enter the 3rd name:"))

list = [a ,b , c]
print(list)

# OR

name.append(a)
name.append(b)
name.append(c)
print(name)

print('--------------------------------------------------------------------------------------------------------------')
# QUESTION 2: CHECK IF A LIST CONTAINS PALINDROME OF ELEMENTS OR NOT
list = []
a = input("Enter the 1st element:")
b = input("Enter the 2nd element:")
c = input("Enter the 3rd element:")

list.append(a)
list.append(b)
list.append(c)

print(list)

cp_list = list.copy()

cp_list.reverse()

if(cp_list == list):
    print("PALINDROME")

else:
    print("NOT PALINDROME")

print('--------------------------------------------------------------------------------------------------------------')
# QUESTION 3: TO COUNT THE NUMBER OF STUDENTS HAVE GRADE A

# grade = []                                                    ---> WHY THIS METHOD IS NOT WORKING ??
# a = input("Enter the marks of 1st student:")
# b = input("Enter the marks of 2nd student:")
# c = input("Enter the marks of 3rd student:") 
# d = input("Enter the marks of 4th student:")
# e = input("Enter the marks of 5th student:")
# f = input("Enter the marks of 6th student:")

# grade.append(a)
# grade.append(b)
# grade.append(c)
# grade.append(d)
# grade.append(e)
# grade.append(f)

# print(grade)
# print()
# print(grade.count(A))

grade = ("A" , "B", 'C', 'A', 'B', 'D', 'E', 'A')

print(grade.count('A'))

print('--------------------------------------------------------------------------------------------------------------')

# QUESTION 4: STORE THE ABOVE TUPLE IN LIST AND SORT IT IN ASCENDING ORDER
# grade = ("A" , "B", 'C', 'A', 'B', 'D', 'E', 'A')                   # WHY ANS IS COMING AS "NONE" ? 

# list = [grade]

# print(list.sort())

grade = ["A" , "B", 'C', 'A', 'B', 'D', 'E', 'A']

grade.sort()

print(grade)
