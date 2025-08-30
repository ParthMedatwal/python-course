#                                       PLEASE REFFER NOTES


#*************** DICTIONARY IN PYTHON *****************#
# dictionaries are a word-meaning pair of information
# In python we call these words as "key" & meanings as "values"
# when we start our searching in python we usually call these "key" to get the "value" stored in it.
# Denoted as :  dict["Key"] = "value"
# Example:

info = {
    "key" : "value",
    "name": "Parth",
    "learning": "Python"
}

print(info)

# Dictionaries are not only limited to strings we can also store other datatype such as int , float, tuple etc.
# Keys can be any datatype, but we cannot use list and dictionary on that place.

print("-------------------------------------------------------------------------------------------------------------------")

#*************** PROPERTIES OF DICTIONARY *****************#
# Dictionaries are unordered, Mutable(changeable) & don't allow duplicating keys
# To call a value stored in a key we can use : dict["name"] = this will give us the value stored in the Key
# To change the value stored in the key we can use: info["name"] = "Yash"
# If we try to make a duplicate key inside a single dictionary then the old value stored in the name will get overwrite by the new value that is stored in the duplicate key with the same name.
# We can also create null dictionaries and then can add values to it later.

print()
print("-------------------------------------------------------------------------------------------------------------------")

#*************** NESTED DICTIONARY *****************#
# Like If-Else was used to create nesting previously, similarly we can use nesting in Dictionary.
# To create a nested dictionary we make a key nested itself inside a dictionary.
# Example:

student = {
    "name" : "Parth",
    "subjects" : {
        "Maths" : 98,
        "Physics": 98,
        "Chemistry": 98
    }
}

print(student)                              # This will print everything inside distionary "student"
print(student["subjects"])                  # This will print only subjects inside distionary "student"
print(student["subjects"]["Chemistry"])     # this will print the value of Chemistry inside distionary "student"

print()
print("-------------------------------------------------------------------------------------------------------------------")

#*************** METHODS IN DICTIONARY *****************#
# There are many moethods of executing operations on a dicttionary some them that are wodely used are:
# 1. myDict.keys():
    # This function gives all the keys used in a dictionary.
    # This does not provide the nested keys made inside an pre-existing key.
    # Example:

print(student.keys())   # o/p : dict_keys(['name', 'subjects'])

print("-------------------------------------------------------------------------------------------------------------------")

# 2. myDict.values():
    # This function gives all the values of the keys used in a dictionary.
    # This provides the value of the main keys & nested key-value pair made inside an pre-existing key-value pair.
    # Example:

print(student.values())   # o/p : dict_values(['Parth', {'Maths': 98, 'Physics': 98, 'Chemistry': 98}])

print("-------------------------------------------------------------------------------------------------------------------")

# 3. myDict.items():
    # This function gives all the key-value used in a dictionary in form of "tuples".
    # Example:

print(student.items())   # o/p : dict_items([('name', 'Parth'), ('subjects', {'Maths': 98, 'Physics': 98, 'Chemistry': 98})])

print("-------------------------------------------------------------------------------------------------------------------")

# 4. myDict.get("key name"):
    # This gives us the value of the key recalled inside the function.
    # this will give "NONE" as the o/p if there is no value or key that exist in the dictionary.
    # Example:  

print(student.get("subjects"))   # o/p : {'Maths': 98, 'Physics': 98, 'Chemistry': 98}
print(student.get("class"))    # o/p : None

print("-------------------------------------------------------------------------------------------------------------------")

# 5. myDict.update(New Dict. name):
    # This is used to add any new key value pair in a pre-existing dictionary.
    # The new key-value pair added to the dictionary will be added after the last key value pair.
    # Example:

student.update({"class" : "10th" })
print(student)   # o/p : {'name': 'Parth', 'subjects': {'Maths': 98, 'Physics': 98, 'Chemistry': 98}, 'class': '10th'}

print()
print("-------------------------------------------------------------------------------------------------------------------")

#*************** SET IN PYTHON *****************#
# Set is the collection of the unordered items.
# Each set is mutable but element in the set must be unique & they are immutable.
# Things that can be stored inside set are: boolean , int , float , str , tuple etc.
# Things that cannot be stored inside a set are: list , Dictionaries.
# In set, each element is in itself is a key and value at the same time.
# Example:

nums = {1,2,3,4,1,2}  
print(nums)         # repeated elements stored only once, so it is resolved to {1,2,3,4}

null_set = {}    # This is an empty set syntax, but this is dictionary 
null_set = set() # This is now a null set.
print(null_set)  # o/p: {}


collection = {1,2,3, "hello" , "world",4}
print(collection)
print(type(collection))

print()
print("-------------------------------------------------------------------------------------------------------------------")
#*************** METHODS IN SET *****************#
# There are several methods that can be performed on a set, some of them are:
# 1. set.add(element):
    # here, we can pass tuple but we cannot pass list and dictionaries.
    # Example:

info = set()

info.add(1)
info.add(2)
info.add(4)
info.add("Parth")

print(info)

print("-------------------------------------------------------------------------------------------------------------------")

# 2. set.remove(element):
    #Example:

info = set()

info.add(1)
info.add(2)
info.add(4)

print(info)

info.remove(4)
print(info)

print("-------------------------------------------------------------------------------------------------------------------")

# NOTE: If we try to add a list in the set , it will give us an Error: "Unhashable value" i.e.. value that are mutable in nature.
        # So, as set elements are immutable i.e.. "Hashable" in nature, hence it will give error.

print("-------------------------------------------------------------------------------------------------------------------")

# 3. set.clear():
    # This will empty the set.
    # Example:

info = set()

info.add(1)
info.add(2)
info.add(4)

print(info.clear())

print("-------------------------------------------------------------------------------------------------------------------")

# 4. set.pop():
    # This will remove random values from the set.
    # Example:

info = set()

info.add(1)
info.add(2)
info.add(4)

print(info.pop())
print(info.pop())

print("-------------------------------------------------------------------------------------------------------------------")

# 4. set X.union(set Y):
    # This will combine different set values and returns a new set.
    # Example:

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))

print("-------------------------------------------------------------------------------------------------------------------")

# 4. set X.intersection(set Y):
    # This will detect common set values and returns a new set.
    # Example:

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.intersection(set2))

print()
print("-------------------------------------------------------------------------------------------------------------------")

#*************** PRACTICE QUESTIONS *****************#

# QUESTION 1 : WAP TO STORE WORD MEANINGS IN A PYTHON DICTIONARY FOR : 
               # (1) TABLE : A WOODEN THING
               # (2) CAT : AN ANIMAL

dict = {
    "TABLE" : "A WOODEN THING",
    "CAT"   :  "AN ANIMAL"
}

print(dict)

print("-------------------------------------------------------------------------------------------------------------------")

# QUESTION 2 : You're given a list of subjects for students. Assume 1 classroom is required for 1 subject. How many classrooms are needed by all students:
               # Subjects are: Python, Java, C, python, javascript, Java, python, Java, C.

subject = {
    "python", "Java", "C", "python", "javascript", "Java", "python", "Java", "C"
}

print(subject)
print("No. of classroom required are: ", len(subject))

print("-------------------------------------------------------------------------------------------------------------------")

# QUESTION 3: WAP To enter marks of three subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. 
              # Use subject name as key and marks as value.

dict = {}

sub1 = int(input("enter marks for Maths: "))
dict.update({"Maths" : sub1})

sub2 = int(input("enter marks for Physics: "))
dict.update({"Physics" : sub2})

sub3 = int(input("enter marks for Chemistry: "))
dict.update({"Chemistry" : sub3})

print(dict)
print("End")

print("-------------------------------------------------------------------------------------------------------------------")

# QUESTION 4: WAP to figure out a way to store 9 and 9.0 as separate values in the set.

set = {
    "float" : 9.0,
    "int" : 9
}

print(set)
