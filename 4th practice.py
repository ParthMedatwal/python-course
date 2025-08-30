dict ={
    'key' : 'value',
    'name' : 'John Doe',
    'roll' : '12345',
    'rank' : 'A'
}

print(dict)

dict1 = {
    'class' : '10th',
    'subject': {
        'math': 99,
        'physics': 95,
        'Chemistry': 98
    }
}

dict1.update({'age': 16})

print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

print(dict1.get('subject'))

nums = {1,2,3,4,5,2,3,1}
print(nums)


null_set = {}
null_set = set()
print(null_set)


collection = {12, "parth", 3.14}
print(collection)
print(type(collection))


nums.add(6)
nums.remove(2)
print(nums)

print(nums.clear())


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))


#question 

dict = {}

a = input("enter the marks for math: ")
dict.update({'math': a})

b = input("enter the marks for physics:")
dict.update({'physics': b})

c = input("enter the marks for chemistry:")
dict.update({'chemistry': c})

print(dict)
print("Thank you")
