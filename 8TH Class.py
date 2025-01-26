#                                       PLEASE REFFER NOTES


#*************** OOPS IN PYTHON *****************#
# To map the real world scenarios, we started using objects in code.
# This is called Object Oriented Programming
# OOPs decreases the redundancy and increase the reuseability of an programm, just like Functions
# In OOPs, we first make classes and then objects inside it

print("-------------------------------------------------------------------------------------------------------------")

#*************** CLASS & OBJECTS IN PYTHON *****************#
# Class is a blueprint for creating objects. Here, we define all the features for an object to work.

# creating Class:
class student:
    name = "Parth Medatwal"
    marks = 94.47

# creating Object(instance):
s1 = student()
print(s1.name)                  # As we defined name in class, so every time when we call name from this class it will show "Parth Medatwal". Hence, it will not change.
print(s1.marks)

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** __init__ Function *****************# 

# Constructor:
# All classes have a function called __init__(), which is always executed when the object is being inititated.

# creating __init__() function:
class student:
    name = "Parth Medatwal"
    marks = 94.47
    def __init__(self):
        print("adding new student in Database...")


s1 = student()              # Result: adding new student in Database..., because it will execute automatically.

print("-------------------------------------------------------------------------------------------------------------")

# def __init__(self), here, self => the object "s1" itself. but we define it like this.

class student:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database...")

n1 = student("Parth")
print(n1.name)              # Result: Parth  i.e.. (Parth will get stored automatically in fullname)

n2 = student("Medatwal")
print(n2.name) 

# In place of self, we can write anything it will work the same but it is recommened to keep it self as it is professional and commonly used
# This self is uniquew for every object made

print("-------------------------------------------------------------------------------------------------------------")

# def __init__(self): ==> This is a Default constructor that have only one parameter
# def __init__(self, fullname): ==> this is a parameterized constructor that have more than one parameters.

print("-------------------------------------------------------------------------------------------------------------")
print()

#*************** ATTRIBUTES *****************# 