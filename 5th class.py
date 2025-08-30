#                                       PLEASE REFFER NOTES


#*************** LOOPS IN PYTHON *****************#
# Loops are used in python to repeat an instruction multiple times.
# there are different types of loops:


# While Loop:
    # In While Loop, the loop continues to work until the condition is true.
    # Example:
        # while True:
        #     print("hello")      # In this example, hello will get printed infinite times because the condition stays true forever.
    # Hence, we need a loop that have a false status at some point to terminate the operation.

c = 1
while c <= 5 :
    print("hello")
    c += 1  
print("-------------------------------------------------------------------------------------------------------------")

# The term "c" here that we used to make the counting start are called as "Iterators"
# The process or the times the process works is called as "Iterations"
# We can also count the number of iterations by:
c = 1
while c <= 10 :
    print("hello", c)
    c += 1
print("-------------------------------------------------------------------------------------------------------------")
#*************** QUESTIONS FOR LOOPS *****************#

# QUESION 1: PRINT NUMBER FROM 1 TO 10
i = 1
while i <= 10:
    print(i)
    i += 1

print("-------------------------------------------------------------------------------------------------------------")

# QUESION 2: PRINT NUMBER in REVERSE FROM 10 TO 1
i = 10
while i >= 1:
    print(i)
    i -= 1

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 3: PRINT A MULTIPLICATION TABLE OF A NUMBER N
n = 3
i = 1
while i <= 10:
    print(n*i)
    i += 1
   
print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 4: PRINT THE SQUARE OF NUMBERS FROM 1 TO 10
i = 1
n = 2

while i <= 10:
    print(i**n)
    i += 1

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 5: PRINT THE ELEMENTS OF THE LIST USING LOOP:
    # ["IRONMAN","THOR","SUPERMAN","BATMAN"]

num = ["IRONMAN","THOR","SUPERMAN","BATMAN"]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1
     
print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 6: SEARCH A NUMBER X IN THIS TUPLE USING LOOP:
    # (1,4,9,16,25,36,49,64,81,100)

num = (1,4,9,16,25,36,49,64,81,100,36)

x = 81
i = 0

while i < len(num):
    if(num[i] == x):
        print("Found at idx: ",i)
    else:
        print("finding...")
    
    i += 1

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** BREAK & CONTINUE IN PYTHON *****************#

# 1.  BREAK: used to terminate the the loop when encountered.
# Example:

i = 1
while i <= 10:
    print(i)
    if ( i == 6):
        break
    i += 1

# To execute break command we need a conditional statement inside which it is written with a condition.

print("-------------------------------------------------------------------------------------------------------------")

# 2. CONTINUE: Terminates execution in the current iteration & continues execution of the loop with the next iteration.
# Example:

# 1. print by skipping 6

i = 1
while i <= 10:
    if ( i == 6):
        i += 1
        continue
    print(i)
    i += 1

print("-------------------------------------------------------------------------------------------------------------")

# 2. print only odd numbers
 
i = 1
while i <= 10:
    if ( i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** FOR LOOP IN PYTHON *****************#
# For Loop are used for the sequential transversal, for travelling through list , string , tuples etc. i.e.. which has an index.
# syntax : for el in list      ; ( list = [1,2,3,4,5])
# Example: 

nums = [1,2,3,4,5,6]

for val in nums:
    print(val)

print("-------------------------------------------------------------------------------------------------------------")

str = "Parth Medatwal"

for char in str:
    print(char)

print("-------------------------------------------------------------------------------------------------------------")

# We can use an ELSE statement with for loop, it is completely optional and is used to print something after completion of the for loop
# Example:

str = "Parth Medatwal"

for char in str:
    print(char)
else:
    print("END")

print("-------------------------------------------------------------------------------------------------------------")

# If we haven't used ELSE then also the code works the same, but ELSE is significantly used for the cases of break.
# Example:

str = "Parth Medatwal"

for char in str:
    if(char == "M" ):
        print("M found")
        break

    print(char)

else:
    print("END")

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** QUESTIONS *****************#

# QUESTION 1: PRINT THE ELEMENTS OF THE LIST USING for LOOP:
    # ["IRONMAN","THOR","SUPERMAN","BATMAN"]

name  = ["IRONMAN","THOR","SUPERMAN","BATMAN"]

for super in name:
    print(super)

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 2: SEARCH A NUMBER X IN THIS TUPLE USING for LOOP:
    # (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
idx = 0

for val in nums:
    if(val == x):
        print("number found at idx", idx)
        break
    idx += 1

else:
    print("END")

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** RANGE IN PYTHON *****************#
# Range function returns a sequence of numbers, starting from 0 (by Default), and increments by 1 (by Default).
# and stops before a specific number.
# Example : range(5) => 0,1,2,3,4   ; start: 0 & step-size: 1 & end: 5

seq = range(5)      # range(stop)

for i in seq:
    print(i)

print("-------------------------------------------------------------------------------------------------------------")

seq = range(2,5)      # range(start,stop)

for i in seq:
    print(i)

print("-------------------------------------------------------------------------------------------------------------")

seq = range(2,10,2)      # range(start,stop,increment by)

for i in seq:
    print(i)

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** QUESTIONS *****************#

# QUESTION 1: Print numbers from 1 to 100

seq = range(1,101)

for i in seq:
    print(i)

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 2: Print numbers from 100 to 1

seq = range(100,0,-1)

for i in seq:
    print(i)

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 2: Print a multiplication table of number n

n = 7

seq = range(7,71)

for i in seq:
    if(i%7 == 0):
        print(i)

# OR

n = int(input("Enter your number: "))

seq = range(1,11)

for i in seq:
    print(n*i)


print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** PASS IN PYTHON *****************#
# Pass is used as a null statement that does nothing. It is used as a place holder for future code.
# Example:

for i in range(5):
    pass

print("some work has done")

# Pass statement is used on the places when the code is needed but we do not want it to run Or to use it for further work.
# Pass can also be used with conditional statement.

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** QUESTIONS *****************#

# QUESTION 1: Write a program to find the sum of first N numbers using while loop

n = int(input("Enter your limit: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
   
print("Total sum is: ", sum)

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 2: Write a program to find the factorial of N numbers using for loop

n = int(input("Enter your limit: "))

fact = 1

for i in range(1 , n+1 ):
    fact *= i

print("factorial is: ", fact)
