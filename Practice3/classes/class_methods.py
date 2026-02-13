#1
class Bank_employees:
    def __init__(self,name,role,age):
        self.name = name
        self.role = role
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age}) - {self.role}"
B1 = Bank_employees("Antonio","IT specialist",29)
print(B1)
#2
class Animals:
    def __init__(self,name,classes,type):
        self.name = name
        self.classes = classes
        self.type = type

    def set_info(self,sc_name):
        self.name = sc_name

A1 = Animals("Wolf","mammal","wild")
A1.set_info("Canis lupus")
print(f"{A1.name} - {A1.classes} - {A1.type}")
3
class Machines:
    def __init__(self,mark,price):
        self.mark = mark
        self.price = price
    def discount(self,discount):
        self.price = self.price * (1- discount/100)
    def watch_to_new_price(self):
        return f"{self.price}"
M1 = Machines("Toyota",6000000)
print(f"{M1.mark} - {M1.price}")
M1.discount(23.9448848484848)
print(M1.watch_to_new_price())
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