# 1
def print_pet_names(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

print_pet_names(Buddy="dog", Felix="cat", Goldie="fish")
#2
def summa(*args):
    summ = 0
    for i in args:
        summ += i;
    return summ
print(summa(9,8,5,4,1,2,6,5))
#3
def whose_capital(**kwargs):
    for capital,country in kwargs.items():
        print(f'{capital} is capital of {country}')
whose_capital(Brasilia="Brasil",Praga='Chehia',Sydney='Australia',Budapesht='Hungary')
#4
def build_filter(**kwargs):
    lst = []
    for key,values in kwargs.items():
        lst.append(f"{key} - {values}")
    return " AND ".join(lst)
print(build_filter(category="books", author="Pushkin", year="1830"))
#5
def profile(name,**info):
    print(f'Profile ------{name.capitalize()}---')
    for key,value in info.items():        
        print(f"{key.replace('_',' ').capitalize()}:{value}")
profile("akyltai",hobby='reading book',age=18,birth_day=24.11)