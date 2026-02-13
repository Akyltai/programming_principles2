class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

data = input().split()
student_name = data[0]
student_gpa = float(data[1])

s = Student(student_name,student_gpa)
s.display()