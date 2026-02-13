#1
class Bank_employees:
    def __init__(self,name,role,age):
        self.name = name
        self.role = role
        self.age = age
B1 = Bank_employees("Antonio","IT specialist",23)
print(f"{B1.name}({B1.age}) - {B1.role}")
#2
class Animals:
    def __init__(self,name,classes,type):
        self.name = name
        self.classes = classes
        self.type = type
A1 = Animals("Wolf","mammal","wild")
print(f"{A1.name} -({A1.classes}) - {A1.type}")
#3
class Machines:
    def __init__(self,mark,price):
        self.mark = mark
        self.price = price
M1 = Machines("Toyota",6000000)
M2 = Machines("Mersedes",12000000)
print(f"{M1.mark} - {M1.price}")
print(f"{M2.mark} - {M2.price}")
#4
class Student:
    def __init__(self,name,university):
        self.name = name
        self.university = university
U1 = Student("Akyltai","KBTU")
print(f"{U1.name} study in {U1.university}")
#5
class Cars:
    def __init__(self,mark,price):
        self.mark = mark
        self.price = price
C1 = Cars("Nissan",6100000)
print(f"{C1.mark} - {C1.price}")