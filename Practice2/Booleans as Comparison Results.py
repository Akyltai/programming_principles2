#First example
if 4>0:
    print("4 bigger then 0")
else:
    print("No")
#Second example 
flag = True
n = int(input(":"))
if n%2 == 0:
    flag = False

if flag:
    print("It's not even")
else:
    print("It's even")
#third example
if True:
    print("It's always true")
else:
    print("It's part of code never will work")
#fourth example
if False:
    print("It's always false,and never will work")
else:
    print("It's part of code always will work")

#Fift example
if 1:
    print("1 it's true")
elif 0:
    print("It's never will work")
else:
    print("Yo")