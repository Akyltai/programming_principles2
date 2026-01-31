#1
a = int(input())
b = int(input())
if a > b: print("a is greater than b")
#2
print('5 bigger then 0') if 5>0 else print("5 not bigger then 0")
#3
c = input(":")
name = c if c[0] == 'A' else "No name"
print(f'{name} ? Oh. Good name.. maybe')
#4
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
#5
age = int(input(":"))
request = "Yes,U can go in" if age>18 else "No,U cannot"
print(request)