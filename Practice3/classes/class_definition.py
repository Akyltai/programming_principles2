#1
class Bank:
    year_of_establish = 1998
#2
my_class = Bank()
print(my_class.year_of_establish)
#3
del my_class
print(type(Bank()))
#4
class Person():
    pass
#5
class Animal():
    wild_animal = "wolves"