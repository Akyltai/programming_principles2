#1 safety way to read file
with open('example.txt','r',encoding="utf-8") as file:
    data = file.read()
    print(data)
#2 second way to read file
f = open('example.txt','r',encoding="utf-8")
content = f.read()
print(content)
f.close()
#3 Safety way to read only one line in file
with open('example.txt','r') as f:
    for line in f:
        print(line.strip())
#4 read first line and write 1 symbol
with open('example.txt','r') as f:
    lines = f.readline()
    print(lines[0])
#5 read file<if it did not exist,rise exception
try:
    with open("missing.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found,try again please.")