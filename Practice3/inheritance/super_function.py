#1
class Machine:
    def __init__(self,model,engine):
        self.model = model
        self.engine = engine
    def get_info(self):
        print(f"{self.model} - {self.engine}")
class Car(Machine):
    pass
M1 = Machine("BMW","BMW34.4")
C1 = Car("Toyota","BMW76")
C1.get_info()
M1.get_info()
#2
class Animal:
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
    def get_info(self):
        print(f"{self.name} - {self.desc}")
class Mammal(Animal):
    pass
class Cows(Mammal):
    pass
#3
class Bank_employees:
    def __init__(self,name,role,age,director):
        self.name = name
        self.role = role
        self.age = age
        self.director = director
class Analys_Departament(Bank_employees):
    def __init__(self, name, role, age, director, finance_data):
        super().__init__(name, role, age, director)
        self._finance_data = finance_data
    def give_finance_status(self):
        print(f"Finance status:{self.finance_data}")

class Creative_Departament(Bank_employees):
    def __init__(self, name, role, age, director, creative_data):
        super().__init__(name, role, age, director)
        self._creative_data = creative_data
    def give_idea(self):
        print(f"Creative idea:{self.creative_data}")    

class Engineering_Departament(Bank_employees):
    def __init__(self, name, role, age, director, technic_resource):
        super().__init__(name, role, age, director)
        self._technic_resource = technic_resource
    def give_idea(self):
        print(f"Number of resource:{self.technic_resource}")  
#4
class Character:
    def __init__(self,name,health,damage,armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def show_HP(self):
        print(f"Character HP: {self.health}")
    
    def show_DMG(self):
        print(f"Character Damage: {self.damage}")
    
    def show_ARM(self):
        print(f"Character Armor: {self.armor}")

class Knights(Character):
    def __init__(self, name, health, damage, armor, attack_skill,extra_armor):
        super().__init__(name, health, damage, armor)
        self._attack_skill = attack_skill
        self._extra_armor = extra_armor

    def double_hit(self):
        self.damage = self.damage * 2

class Wizard(Character):
    def __init__(self, name, health, damage, armor, magic_damage, intellegence):
        super().__init__(name, health, damage, armor)
        self._magic_damage = magic_damage
        self._extra_armor = intellegence

    def fireball(self):
        self.damage = self.damage * 5
    
#5
class Transport:
    def __init__(self, model, plate_number, max_payload, driver_name):
        self.model = model
        self.plate_number = plate_number
        self.max_payload = max_payload
        self.driver_name = driver_name

class CargoTruck(Transport):
    def __init__(self, model, plate_number, max_payload, driver_name, cargo_type):
        super().__init__(model, plate_number, max_payload, driver_name)
        self._cargo_type = cargo_type

    def check_cargo(self):
        print(f"Грузовик {self.model} везет тип груза: {self._cargo_type}")

class CourierBike(Transport):
    def __init__(self, model, plate_number, max_payload, driver_name, battery_capacity):
        super().__init__(model, plate_number, max_payload, driver_name)
        self._battery = battery_capacity

    def check_battery(self):
        print(f"Bike battery {self.driver_name}: {self._battery}%")

class RefrigeratedVan(Transport):
    def __init__(self, model, plate_number, max_payload, driver_name, temperature):
        super().__init__(model, plate_number, max_payload, driver_name)
        self._temperature = temperature

    def get_thermal_report(self):
        print(f"Refregirator temperature {self.plate_number}: {self._temperature}°C")