#1
class Animal:
    def make_sound(self):
        print("Some generic animal sound")
class Dog(Animal):
    def make_sound(self):
        print("Bark! Bark!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
#2
class Payment:
    def process(self, amount):
        print(f"Processing a payment of ${amount}")
class CreditCardPayment(Payment):
    def process(self, amount):
        print(f"Validating card... Charging ${amount} with 2% fee.")
class CryptoPayment(Payment):
    def process(self, amount):
        print(f"Verifying blockchain transaction for ${amount}...")
#3
class FileReader:
    def read(self):
        print("Reading raw bytes from file...")
class PDFReader(FileReader):
    def read(self):
        print("Extracting text and images from PDF layout...")
class CSVReader(FileReader):
    def read(self):
        print("Parsing rows and columns from spreadsheet...")
#4
class Employee:
    def calculate_salary(self):
        return 3000
class Manager(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 2000
#5
class UIElement:
    def draw(self):
        print("Drawing a generic UI shape.")

class Button(UIElement):
    def draw(self):
        print("Drawing a clickable button with a label.")

class Checkbox(UIElement):
    def draw(self):
        print("Drawing a small square box for selection.")