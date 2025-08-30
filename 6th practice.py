a = 5
b = 2

sum = a + b
print(sum)

# Functions:

def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

# Now:

calc_sum(2,2)
calc_sum(5,10)

def calc_pr(a = 4, b = 2):
    print(a*b)
    return a*b


calc_pr() # this will give 8 as o/p becuase we passed the arguments in the starting of the code when we defined functions

def calc_pr1(a , b = 2):
    print(a*b)
    return a*b

calc_pr1(2) # this will give 4 as o/p because we passed only one argument in b so it will take the same value for a while giving the answer

# def calc_pr2(a = 4, b):    # this will give us error as the second argument is not given a default value which is against the rules of defining a function
#     print(a*b)
#     return a*b


a = [1,2,3,4,5,6,7,8,9]
b = [13,14,15,16,17,18,19]

def len_list(lst):
    print(len(lst))
    return len(lst)


print(len_list(a))      # this will give us 10 as o/p
print(len_list(b))      # this will give us 7 as o/p


num = [1,2,3,4,5,6,7,8,9,3,2,4,5,8]

def pr_list(lst):
    for i in lst:
        print(i, end = " ")
    return lst

pr_list(num)  #This will print all the elements of the list in a single line


def fact_n(fact):
    if fact == 0:
        return 1
    else:
        return fact * fact_n(fact-1)

num = int(input("Enter a number: "))
print(fact_n(num))          # this will give the factorial of the number 3 as 6 or it depends on the input given by the user


def usd_inr(cur):
    print(cur * 80)
    return cur * 80


print(usd_inr(100))     # this will give as o/p as 8000


def odd_even(num):
    if(num%2 == 0):
        print("Even")
    else:
        print("Odd")
    return 

a = int(input("Enter a number: "))
odd_even(a)     # this will give us the result as even or odd depending upon the number entered by the user



# Recursion:

def show(n):
    print(n)

show(5) # This will print "Hello" 5 times, hence recursion happened i.e.., something keeps going on repeat until it reaches the base case.

def show(n):
    if n == 0:
        return
    else:
        print("Hello")
        show(n-1)

show(10) # This will print numbers backward from 10 to 1


def fact(n):
    if (n ==0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

fact(3)     # this should give us 6 ie.., 3x2x1 = 6


def calc_sum(n):
    if n == 0:
        return 0
    else:
        return n + calc_sum(n-1)

calc_sum(3)     # this will give us the o/p as 6 i.e.., 3+2+1 = 6

num1 = [1,2,3,4,5,6,7,8,9]


def pr_list(list, idx =0):
    if(idx == len(list)):
        return 0
    else:
        print(list[idx], end = " ")
        return pr_list(list, idx + 1)

pr_list(num1)     # this will print 1 2 3 4 5 6 7 8 9

