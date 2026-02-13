#1
a = list(filter(lambda x:(x>6),(10,221,39,5)))
print(a)
#2
b = filter((lambda x:x%2==0),[1,2,34,5,6,78])
print(list(b))
#3
c = filter((lambda x:x==x.capitalize()),(["Akyltai","want","4","GPA"]))
print("Correct capital words:")
for i,j in enumerate(c):
    print(f'N{i} - {j}')
#4
d = filter((lambda x:x.isdigit()),(["Yo","7","4.5","23"]))
print("Digit is:")
print(list(d))
#5
f = filter((lambda x:x>5),(3,4,5,1,6,7,8))
print(*f)