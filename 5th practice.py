# while loop

i = 1

while i <=10:
    if(i%2!=0):
        print(i)
    i += 1

c = 10
while c >=1:
    print(c)
    c -= 1

a = 3
b = 1

while b <= 10:
    print(a*b)
    b += 1

m = 1
n = 3

while m <=10:
    print(m**n)
    m += 1


names = ["Alice", "Bob", "Charlie"]
idx = 0

while idx < len(names):
    print(names[idx])
    idx += 1


nums = [1,2,3,4,5,6,7,8,9,10]

x = 8
i = 0

while i < len(nums):
    if (nums[i] == x):
        print("Found x at:", i)
        break
    else:
        print("finding...")
        
    i += 1


num = [1,2,3,4,5,6,7,8,9,10]

x = 6
i = 0

while i < len(num):
    if (i == 6):
        print("found x at: ", i)
        i += 1
        continue
    print(i)
    i += 1


# for loop


for val in nums:
    print(val)


str = "Parth Medatwal"

for char in str:
    print(char)

for char in str:
    if (char == "w"):
        print("Found W at index:", str.index(char))
        break
    print(char)

else:
    print("No M found")


# Range

seq = range(1,11)
for num in seq:
    print(num)


seq = range(10,0,-1)
for num in seq:
    print(num)


a = int(input("Enter the number: "))

seq = range(1, 11)

for i in seq:
    print(a*i)


num = int(input("enter a number: "))

sum = 0
i = 1

while i <= num:
    sum += i
    i += 1

print("The sum is: ", sum)


n = int(input("enter a number: "))
fact = 1

for i in range(1, n +1):
    fact *= i
print("The factorial is: ", fact)