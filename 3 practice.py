marks = [85, 90, 78, 92, 88]
average = sum(marks) / len(marks)
print("The average mark is:", average)

print(type(marks))
print(len(marks))
print(marks[2])
print(marks[1])
print(marks[:len(marks)])

marks[0] = 95
print("The updated marks are:", marks)

list1 = [0 , 1 , 2 , 3]

list1.append(4)
list1.sort()
list1.sort(reverse=True)
list1.reverse()
list1.remove(2)
list1.pop()
list1.pop(1)
list1.insert(3, "parth")
print(list1.index(0))

tup = (0, 1, 2, 3)

print(type(tup))
print(len(tup))
print(tup[2])
print(tup[1])
print(tup[:len(tup)])
print(tup.index(2))

# check if it is palindrome or not
list = []

a = input("Enter something: ")
b = input("Enter something: ")
c = input("Enter something: ")

list.append(a)
list.append(b)
list.append(c)

print(list)

cp_list = list.copy()

cp_list.reverse()

if(list == cp_list):
    print("The entered strings are a palindrome.")
else:
    print("The entered strings are not a palindrome.")