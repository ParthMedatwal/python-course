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
    def __init__(self):     # def __init__(self), here, self => the object "s1" itself. but we define it like this.
        print("adding new student in Database...")


s1 = student()              # Result: adding new student in Database..., because def __init__(self) will execute automatically.

print("-------------------------------------------------------------------------------------------------------------")


class student:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database...")

n1 = student("Parth")
print(n1.name)              # Result: Parth  i.e.. (Parth will get stored automatically in fullname)

n2 = student("Medatwal")    # Result: Medatwal i.e.. (Medatwal will get stored automatically in fullname)
print(n2.name) 

# In place of self, we can write anything it will work the same but it is recommened to keep it self as it is professional and commonly used
# This self is unique for every object made

print("-------------------------------------------------------------------------------------------------------------")

# def __init__(self): ==> This is a Default constructor that have only one parameter
# def __init__(self, fullname): ==> this is a parameterized constructor that have more than one parameters.

print("-------------------------------------------------------------------------------------------------------------")
print()

class student:
    college_name = "ABC College"
    name = "Anonymous"

    def __init__(self, fullname, marks, age):
        self.name = fullname
        self.marks = marks
        self.age = age
        print("adding new student in Database...")

n1 = student("Parth", 94.47, 14)
print(n1.name, n1.marks, n1.age)            # Result: Parth 94.47 14 will get stored automatically in object
                                            
                                            
n2 = student("Medatwal", 85.50, 15)    
print(n2.name, n2.marks, n2.age)            # Result: Medatwal 85.50 15 will get stored automatically in fullname

print("--------------------------------------------------------------------------------------------------------------")

#*************** CLASS & INSTANCE ATTRIBUTES *****************# 
# Attributes are the variables that belong to a class.
# In the above example: name, marks, and age are attributes of the student class.

# CLASS attributes are common for every object
# INSTANCE attributes are unique for each object

# In above example n1 and n2 are two different objects, so their attributes are also different. & self.name, self.marks, self.age are INSTANCE attributes because they are different for each student.
# If we define any attribute outside the __init__ function, then it will be a CLASS attribute because it will be common for every object, above it was "student".

print(student.college_name)       # Result: ABC College will get printed & it is better to define it once as it is CLASS attribute and storing it again and again will cause us memory issues.


# Object attributes > Class attributes --> preference level whenever class & object attributes have same value

print(s1.name)                  # Result: " Parth " & not " Anonymous " because of preference level, we usually use it in scenarios where user doesn't provide full info. to the system.


print("--------------------------------------------------------------------------------------------------------------")

#*************** METHODS *****************# 

# CLASS is made up of two things ie.. attributes & methods
# METHODS are functions defined inside a class that operate on instances of that class.
# They are used to perform operations on the data (attributes) of the class.
# METHODS can also modify the state of the object (instance) by changing its attributes.
# METHODS can be called on an instance of the class using the dot notation.
# For example: instance.method_name()

class student:
    college_name = "ABC College"
    name = "Anonymous"

    def __init__(self, fullname, marks, age):    # this is a Method
        self.name = fullname
        self.marks = marks
        self.age = age
        print("adding new student in Database...")

    def welcome(self):      # this is a Method
        print(f"Welcome {self.name} to {student.college_name}!")
    
    def get_marks(self):    # this is a Method
        print(f"{self.name}'s marks are: {self.marks}")


n1 = student("Parth", 94.47, 14)
n1.welcome()
n1.get_marks()

print()

n2 = student("Yash", 85.50, 15)
n2.welcome()
n2.get_marks()

print("--------------------------------------------------------------------------------------------------------------")

#*************** Questions *****************#

# Question 1: Create Student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average marks.

class student:
    def __init__(self, name, math, phy, che):
        self.name = name
        self.math = math
        self.phy = phy
        self.che = che

    def pr_avg(self):
        avg = (self.math + self.phy + self.che) / 3
        print(f"{self.name}'s average marks are: {avg}")

name = input("Enter student's name: ")
math = float(input("Enter marks for Math: "))
phy = float(input("Enter marks for Physics: "))
che = float(input("Enter marks for Chemistry: "))

s1 = student(name, math, phy, che)
s1.pr_avg()

print("--------------------------------------------------------------------------------------------------------------")

#*************** STATIC METHODS *****************# 

# Methods that don't use self parameter in the function.
# They are defined using the @staticmethod decorator.
# They can be called on the class itself, rather than on instances of the class.
# Static methods do not have access to the instance (self) or class (cls) variables.
# They can only access the parameters passed to them.
# They are used for utility functions that perform a task in isolation.
# Static methods are not dependent on class or instance variables.

class student:

    @staticmethod
    def college():
        print("welcome to ABC College")


print("--------------------------------------------------------------------------------------------------------------")

#*************** ABSTRACTION & ENCAPSULATION *****************# 

# ABSTRACTION: Hiding the implementation/unnesessary details of a class and only showing the essential features to the user.

class car:                              # ------------
    def __init__(self):                 #            |
        self.acc = False                #            |
        self.brk = False                #            |
        self.clutch = False             #            |
                                        #            |----------> This is the actual/main mechanism that is hidden behind starting the car. This is Encapsulation!! 
    def start(self):                    #            |
        self.clutch = True              #            |
        self.acc = True                 #            |
                                        #            |
        print("Car started...")         # ------------         

car1 = car()    # -------
                #        |----> This is out of the CLASS statements and all the info. is hidden in CLASS. This is called Abstraction !!
car1.start()    # -------


# ENCAPSULATION: Wrapping data(attributes) and the functions(Methods) into a single unit called as object.

print("--------------------------------------------------------------------------------------------------------------")

#*************** Questions *****************#

# Question 2: Create an Account class with two attributes balance and account number. Create methods for debit, credit and printing the balance.

class account():
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print(f"{amount} was debited; New Balance is: {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} was credited; New Balance is: {self.balance}")

    def acc_details(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Current Balance: {self.balance}")

print()

acc_no = input("enter your account number: ")
debit_amount = float(input("enter amount to debit: "))

print()

detail = account(1000, acc_no)
detail.acc_details()
detail.debit(debit_amount)

print()

detail.acc_details()
credit_amount = float(input("enter amount to credit: "))
detail.credit(credit_amount)

print("--------------------------------------------------------------------------------------------------------------")

#*************** del KEYWORD *****************#

# The del statement is used to delete objects in Python.
# It can be used to delete variables, lists, or even class instances.
# Once an object is deleted, it cannot be accessed again.

class name():

    def __init__(self,name):
        self.name = name


your_name = input("enter your name: ")

s1 = name(your_name)

print(s1.name)          # Result: yash or anything we put here
del s1
# print(s1.name)          # Result: error, because s1 is deleted

print("--------------------------------------------------------------------------------------------------------------")

#*************** PRIVATE(LIKE) ATTRIBUTES & METHODS *****************#

# Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
# Object Oriented Programming works differently in Python compared to other programming language and in Python it is generally conceptual implementations.
# We make attributes private by adding a double underscore prefix. i.e.., __attribute_name

class person():

    __name = "anonymous"

    def __Hello(self):
        print("Hello Person!")

    def Welcome(self):
        self.__Hello()


p1 = person()

print(p1.Welcome())                  # Result: Hello Person! will be printed because this method/function was not made private.
print(p1._person__Hello())           # Result: throws error because cannot be accessed made private

print("--------------------------------------------------------------------------------------------------------------")

#*************** INHERITANCE *****************#

# When one class(children/derived) inherits/derives/takes the properties and methods of another class(parent/base), it is called inheritance.
# Inheritance allows for code reusability and the creation of a hierarchical relationship between classes.
# The derived class can access the attributes and methods of the base class.
# The base class can be used to define common behavior that can be shared across multiple derived classes.

# Example of Single Inheritance:
class Animal:                       # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):                  # Child class
    def speak(self):                # features inherited from Animal
        print(f"{self.name} barks.")

class Cat(Animal):                  # Child class
    def speak(self):                # features inherited from Animal
        print(f"{self.name} meows.")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

print()

# ************ TYPES OF INHERITANCE:

# Single Inheritance , Multi-level Inheritance, Multiple Inheritance

# Single Inheritance: One class inherits from another.
# Multi-level Inheritance: A class inherits from a derived class, forming a chain.
# Multiple Inheritance: A class inherits from multiple base classes.
# Hierarchical Inheritance: Multiple classes inherit from a single base class.
# Multi-Parent Inheritance: A class can have multiple parent classes.

# Example of Multiple Inheritance:
class Father:
    def skills(self):
        print("Father's skills")

class Mother:
    def hobbies(self):
        print("Mother's hobbies")

class Child(Father, Mother):
    def details(self):
        print("Child's details")

c = Child()
c.skills()
c.hobbies()
c.details()

print()

# Example of Multi-level Inheritance:
class Grandfather:
    def traits(self):
        print("Grandfather's traits")

class Father(Grandfather):
    def skills(self):
        print("Father's skills")

class Child(Father):
    def details(self):
        print("Child's details")

c = Child()
c.traits()
c.skills()
c.details()


print("--------------------------------------------------------------------------------------------------------------")

#*************** SUPER METHOD *****************#

# The super() function is used to call a method from a parent class.
# It allows you to access inherited methods that have been overridden in a child class.


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call the parent class method
        print("Dog barks")

dog = Dog()
dog.speak()


print("--------------------------------------------------------------------------------------------------------------")

#*************** CLASS METHOD *****************#

# A class method is a method that is bound to the class and not the instance of the class.
# It can modify class state that applies across all instances of the class.
# Class methods are marked with the @classmethod decorator.

class MyClass:
    class_variable = 0

    @classmethod
    def class_method(cls):
        cls.class_variable += 1
        print(f"Class variable incremented to: {cls.class_variable}")

MyClass.class_method()
MyClass.class_method()

print("--------------------------------------------------------------------------------------------------------------")

#*************** PROPERTY DECORATORS *****************#

# Property decorators are a way to manage the attributes of a class.
# They allow you to define methods in a class that can be accessed like attributes.
# The @property decorator is used to define a getter method,
# and the @<property_name>.setter decorator is used to define a setter method.

# EXAMPLE:

class student():
    def __init__(self, phy, math, che):
        self.phy = phy
        self.math = math
        self.che = che
        self.percentage = str((phy + math + che) / 3)

stu1 = student(85, 90, 80)
print(stu1.percentage)          # this will print the percentage without any issues

# but

# Lets say that teachers wants to change the percentage of the student and then print the updated percentage

stu1.phy = 66
print(stu1.percentage)          # this will still print the old percentage and not the updated one, to solve this problem we can use property decorators

# property method will allow us to dynamically calculate the percentage whenever it is accessed

# Correct method: 

class student():
    def __init__(self, phy, math, che):
        self.phy = phy
        self.math = math
        self.che = che

    @property
    def percentage(self):
            return str((self.phy + self.math + self.che) / 3)
    
stu1 = student(85, 90, 80)
print(stu1.percentage) 

stu1.phy = 66
print(stu1.percentage)       # now this will print the updated percentage


print("--------------------------------------------------------------------------------------------------------------")

#*************** POLYMORPHISM *****************#

# Polymorphism allows methods to do different things based on the object it is acting upon.
# It is often used in conjunction with inheritance.
# It allows for methods to be used in a way that is independent of the specific class of the object.
# This is achieved through method overriding.



# basic example:
class Bird:
    def sound(self):
        print("Chirp")

class Dog:
    def sound(self):
        print("Bark")

def animal_sound(animal):
    animal.sound()

bird = Bird()
dog = Dog()

animal_sound(bird)
animal_sound(dog)


print("--------------------------------------------------------------------------------------------------------------")

# Question: WAP to add two complex numbers using OOPS

class Complex():
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_num(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, other):               # Here, we define the addition logic for this question and class
        new_real = self.real + other.real
        new_img = self.img + other.img
        return Complex(new_real, new_img)

    def __sub__(self, other):               # Here, we define the subtraction logic for this question and class
        new_real = self.real - other.real
        new_img = self.img - other.img
        return Complex(new_real, new_img)


num1 = Complex(2, 3)
num1.show_num()

num2 = Complex(4, 5)
num2.show_num()

result = num1 + num2
result.show_num()

result = num1 - num2
result.show_num()


print("--------------------------------------------------------------------------------------------------------------")

#*************** PRACTICE QUESTIONS *****************#

# 1. define a circle to create a circle with radius R using the constructor. define an area method of the circle which calculate the area of the circle. define a parameter method of the class which allows to calculate the parameter of the circle.

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius * self.radius

    def Perimeter(self):
        return 2 * 3.14 * self.radius
    
area1 = Circle(5)
print(area1.Area())
print(area1.Perimeter())

peri1 = Circle(5)
print(peri1.Area())
print(peri1.Perimeter())

print ()

# 2. define Employee class with attributes role, department and salary. this class also has a show details() method. create an engineer class that inherits property from Employee and has additional attribute name & age.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print("Role: ", self.role)
        print("Department: ", self.department)
        print("Salary: ", self.salary)

class Engineer(Employee):

        def __init__(self, name, age):
            self.name = name
            self.age = age
            super().__init__("Engineer", "IT", "75000")


e1 = Engineer("Alice", 30)
e1.show_details()

print()

# 3. create a class called order which stores item and its price. use dunder function __gt()__ to convey that: order1 > order2 id the price of order1 > order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):        # defining the greater than operator logic, for which __gt__() is used
        return self.price > other.price

p1 = Order("Item1", 300)
p2 = Order("Item2", 200)

print(p1 > p2)
