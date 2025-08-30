#                                       PLEASE REFFER NOTES


#*************** FUNCTIONS IN PYTHON *****************#
# Function is a block of statement that perform a specific task.
# If we create a function we can use it n number of times to perform the same task.
# A function is created by:   def function_name():
# Example: 

a = 5 
b = 10

sum = a + b
print(sum)          # Result: 15

# This can be required to write for a long code which makes it typical and time consuming, So we use Function instead.

def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum          # The function is being created, & called as FUNCTION DEFINITION
    
    # OR

# We can also use this format to def function

#   def calc_sum(a,b):
#       print(a + b)
#       return a + b          --> this will do the same job

# Now we can use this multiple times in long set of codes.

calc_sum(2,2)           # Result: 4
calc_sum(1,11)          # Result: 12
calc_sum(15,20)         # Result: 35
calc_sum(5,5)           # Result: 10 
calc_sum(15,11)         # Result: 26

# Here, a & b               --> Parameters
#       calc_sum(a,b):      --> Function call
#       (2,2)               --> Arguments, which later stored in Parameters.

# Example 2 :

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()           # Hello will be printed 5 times

# The function made above does not take any i/p and does not return any o/p.
# So, when we'll try to print the value of print_hello(), it will give o/p as NONE.

output = print_hello()
print(output)           # Result: NONE

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** TYPES OF FUNCTION *****************#

# 1. BUILD-IN FUNCTIONS:
    # These are the function that are predefined in Python.
    # Example: print() , len() , range() , type() etc.

# 2. USER DEFINED FUNCTIONS:
    # These are the functions that are made by the user on need.
    # Example: calc_sum etc.

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** DEFAULT PARAMETERS *****************#

# Default parameters are the values that are given to the function that are used when NO arguments are passed while writing a code.
# Example: 

# calc_sum()    ---> this will give an error whenever we try to pass null ARGUMENT, because function consist some parameters but argument are not given to fulfill it.

# So, to solve this issue we use DEFAULT PARAMETERS.

# Example 1:
def cal_pr( a= 4, b=2 ):
    print(a * b)
    return a * b

cal_pr()     # Result: 8

# Example 2:
def cal_pr( a, b=2 ):
    print(a * b)
    return a * b

cal_pr(2)     # Result: 4 , because: a = 2 & b = 2

# Example 3:
# def cal_pr( a = 2, b ):
#     print(a * b)
#     return a * b                  --> Error on line 100, because "a" can stay undefined but not "b", according to rules.


print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** QUESTIONS *****************#

# QUESTION 1: Write a function to print the length of a list. (List is the parameter).

num = [0,1,2,3,4,5,6,7,8,9]

def print_len(list):
    print(len(list))
    return(list)

print_len(num)

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 2: Write a function to print the elements of a list in a single line.(List is the parameter).

num = [0,1,2,3,4,5,6,7,8,9]

def print_list(num):
    for item in num:
        print(item, end="")

print_list(num)
print()

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 3: Write a function to find the factorial of N.(N is the parameter)

n = int(input("Enter your number: "))

def fact_n(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

fact_n(n)

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 4: Write a function to convert USD to INR.

n = int(input("Enter your amount: "))
i = int(82)

def usd_inr(n):
    print(n*i)

usd_inr(n)

print("-------------------------------------------------------------------------------------------------------------")

# QUESTION 5: Write a function that gives "odd" for odd number passed as input and same for even.

num = int(input("Enter your number: "))

def odd_even(num):
    if (num%2 == 0):
        print("Even")
    else:
        print("Odd")

odd_even(num)

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** RECURSSION *****************#
# When a function calls itself repeatedly in set of codes
# Recurssions are same as loops and the work can be done by using both
# Example: 

def show(n):
    print(n)

show(5)         # Result: 5

print("-------------------------------------------------------------------------------------------------------------")

# what if we want to print numbers from 5 to 1 backwards ?
    # So, we will use Recurssion although loops can also be used

def show(n):
    if(n == 0):                 # This is a "Base Case" which will terminate the loop, after 0 is reached.
        return
    print(n)
    show(n-1)

show(5)         # Result: 5 , n-1 = 4, n-2 = 3 , n-3 = 2 , n-4 = 1
                # Here, after every iteration "n gets updated with the last result"

print("-------------------------------------------------------------------------------------------------------------")

# Question: WAP to perform factorial using recurssion

def fact(n):
    if(n == 0 or n == 1):               # This is the base case which says that when the value reaches 0 or 1 return 1 as output, because 0! & 1! is 1.
        return 1
    else:
        return n * fact(n-1)


print(fact(5))

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** QUESTIONS *****************#

# Question 1: Write a recursive function to calculate the sum of first N natural numbers.

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
    

print(sum(4))

print("-------------------------------------------------------------------------------------------------------------")

# Question 2: Write a recursive function to print all elements in a list.(Use list and index as parameters)

list = [1,2,3,4,5]

def pr_el(list,idx=0):
    if(idx == len(list)):
        return 0
    print(list[idx])
    pr_el(list, idx+1)

pr_el(list)