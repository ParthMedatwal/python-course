f = open("file.txt", "w")
f.write("Hello, world!")
f.close()

f = open("file.txt", "r")
content = f.read()
print(content)
print(type(content))
f.close()

import os

# Remove file1.txt if it exists before creating it in 'x' mode
if os.path.exists("file1.txt"):
    os.remove("file1.txt")

d = open("file1.txt", "x")
d.write("Hello, world!\n" "12345\n" "Parth")
d.close()

d = open("file1.txt", "r")
content = d.read()
print(content)
print(type(content))
d.close()

d = open("file1.txt","r")
line1 = d.readline()
print(line1)
line2 = d.readline()
print(line2)
d.close()

f = open("file1.txt","w")
content = f.write("This is new line")
print(content)
f.close()

f = open("file1.txt","a")
content = f.write("\n Parth Medatwal")
print(content)
f.close()

with open("sample.txt","w") as f:
    data = f.write("Parth Medatwal")
    data = f.write("\n 12345")
    data = f.write("\n Hello World")
    print(data)

with open("sample.txt","r") as f:
    data = f.read()
    print(data)


os.remove("sample.txt")


a = open("example.txt","w")
data = a.write("This is example file")
print(data)
a.close()

a = open("example.txt","r")
data = a.read()
print(data)
new_data = data.replace("example","sample")
print(new_data)
a.close()


word = "learning"

with open("example.txt","r") as num:
    if(word in num.read() != -1):
        print("Word found")
    else:
        print("not found")


with open("sample.txt", "a") as f:
    data = f.write("\nusing this i can do anything")
    print(data)

    with open("sample.txt", "r") as f:
        content = f.read()
        print(content)



word = "using"

def check_for_line(data):
    word = "using"
    data = True
    line_no = 1

    with open("sample.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                line_no += 1
    
    return -1           # this means if not found then return -1 as o/p


with open("sample.txt","w") as f:
    data = f.write("\n1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    print(data)

count = 0

with open("sample.txt","r") as f:
    data = f.read()
    print(data)

    num = data.split(",")
    for val in num:
        if(int(val)%2==0):
            count += 1

    print(count)


