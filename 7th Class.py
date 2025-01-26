#                                       PLEASE REFFER NOTES


#*************** FILE I/O IN PYTHON *****************#
# Python can be used to perform operations in the file.(read & write)
# Type of files in python:
# 1. Text files: files that have characters stored in it i.e.. .txt , .docx , .log etc.
# 2. Binary files: files that have info. stored in form of anything except characters i.e.. .mp4 , .mov , .png etc.

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** OPEN , READ & CLOSE FILE *****************#   
# We have to open a file before reading & writing.

# example:

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

print("-------------------------------------------------------------------------------------------------------------")
#*************** CHARACTERS & MEANING *****************#
# r = open for reading(default)
# w = open for writing i.e.. truncate or overwrite (it deletes the previous data and update it with new)
# x = create a new file and open it for writing
# a = open for writing, appending to the end of the file if it exist 
# b = binary mode
# t = text mode(default)
# + = open a disk file for updating(reading and writing)

# data = f.read() => reads entire file or we can specify the point to which it should read

f = open("demo.txt","r")
data = f.read(5)
print(data)

f.close()

print("-------------------------------------------------------------------------------------------------------------")

# data = f.readline() => reads one line at a time

f = open("demo.txt","r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

print("-------------------------------------------------------------------------------------------------------------")

# after implementing data = f.read(), if we will try to perform readline() it will give empty spaces. Because after reading all the data we now are at end, and there is nothing to print except empty spaces
# example:
f = open("demo.txt","r")
data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()                     

print("-------------------------------------------------------------------------------------------------------------")

# f.write(""):
f = open("demo.txt","w")
data = f.write("fhagsba")
print(data)

print("-------------------------------------------------------------------------------------------------------------")

# 
f = open("demo.txt","a")
data = f.write("\n osdhvodinv")
print(data)

print("-------------------------------------------------------------------------------------------------------------")

# f.write can also create new files for us if it does not existed before. Also works when we use append "a" in place of "w"
# Example:

f = open("sample.txt","w")
data = f.write("Parth Medatwal")
print(data)

print("-------------------------------------------------------------------------------------------------------------")

#*************** Read article provided for using 2 methods simultaneously *****************#

print()
print("-------------------------------------------------------------------------------------------------------------")

#*************** WITH SYNTAX IN PYTHON *****************#
# With is a file i/o syntax that is used to execute the program with using an alias.
# it does not need a closing statement
# example:

with open("sample.txt","r") as f:
    data = f.read()
    print(data)

with open("sample.txt","w") as f:
    data = f.write("kjsbdjfb")
    print(data)

print()
print("-------------------------------------------------------------------------------------------------------------")

#*************** DELETING FILE IN PYTHON *****************#
# We use the os module
# Module (like a code library) is a file written by another programmer that generally hs a functions we can use

import os
os.remove("sample.txt")         # this will remove the file named as sample.txt we created before

print()
print("-------------------------------------------------------------------------------------------------------------")

#*************** QUESTIONS *****************#

# Question 1: Write a new file practice txt using python,add the following data in it
# Hi everyone
# We are learning file I/O
# using java
# i like programming in java

with open("practice.txt","w") as f:
    data = f.write("Hi everyone\nWe are learning file I/O\nusing java\ni like programming in java")
    print(data)

print("-------------------------------------------------------------------------------------------------------------")

# Question 2: Write a function that replace all occurrences of Java with python in above file

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

print("-------------------------------------------------------------------------------------------------------------")

# Question 3: Search if the word learning exists in the file or not

word = "learning"

with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):              # This means if word does not exist we get -1 as index by default, which should not come as a result
        print("Found")
    else:
        print("Not found")

print("-------------------------------------------------------------------------------------------------------------")

# Question 4: Height function to find in which of the file does the word using occur first. Print one if word not found

def check_for_line():
    word = "using"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
        
    return -1

check_for_line()

print("-------------------------------------------------------------------------------------------------------------")

# Question 5: From file containing numbers separated by print the count of even numbers

# we will use the split function that already exists in python

count = 0
with open("practice.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)                        # Result: 4 , it will not work as previous code will overwrite the data.