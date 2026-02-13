class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = int(base_salary)

    def total_salary(self):
        return float(self.base_salary)

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = int(bonus_percent)

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)

class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = int(completed_projects)

    def total_salary(self):
        return self.base_salary + (self.completed_projects * 500)

class Intern(Employee):
    pass

data = input().split()
role = data[0]
name = data[1]
base_salary = int(data[2])


if role == "Manager":
    bonus_percent = int(data[3])
    emp = Manager(name, base_salary, bonus_percent)
elif role == "Developer":
    projects = int(data[3])
    emp = Developer(name, base_salary, projects)
else:
    emp = Intern(name, base_salary)
print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")