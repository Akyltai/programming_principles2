#1
for i in range(1,11):
    print(i,end=" ")
#2
print('\n')
vitamines = ['A','B','C+']
for i in vitamines:
    print(i)
#3
meel = ['ramen','plov','borsch']
for i,j in enumerate(meel):
    print(i,"-",j,sep=" ",end=" ||")
#4
str = "It's so good to be an AC specialist"
for i in str:
    print(i,end=".")
#5
n = int(input(":"))
m = int(input(":"))
print("Odd numbers from 'n' to 'm")
for i in range(n,m+1,2):
    print(i)