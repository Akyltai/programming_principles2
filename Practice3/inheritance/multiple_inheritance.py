#1
class Flyer:
    def fly(self):
        print("Flying high in the sky!")
class Swimmer:
    def swim(self):
        print("Swimming in the deep water!")
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack quack!")
donald = Duck()
donald.fly()
donald.swim()
#2
class Phone:
    def call(self):
        print("Dialing a number...")
class Camera:
    def take_photo(self):
        print("Click! Photo saved.")
class SmartPhone(Phone, Camera):
    def browse_internet(self):
        print("Opening browser...")
iphone = SmartPhone()
iphone.call()
iphone.take_photo() 
#3
class A:
    def say(self):
        print("A")
class B(A):
    def say(self):
        print("B")
class C(A):
    def say(self):
        print("C")
class D(B, C):
    pass
obj = D()
obj.say()
#4
class Knight:
    def shield_block(self):
        print("Blocking with a heavy shield!")
class Healer:
    def cast_heal(self):
        print("Healing wounds...")
class Paladin(Knight, Healer):
    def holy_strike(self):
        print("Attacking with holy light!")
uther = Paladin()
uther.shield_block()
uther.cast_heal()
#5
class Employee:
    def work(self):
        print("Doing daily tasks.")
class StockHolder:
    def vote(self):
        print("Voting on company decisions.")
class Manager(Employee, StockHolder):
    def manage_team(self):
        print("Leading the team...")