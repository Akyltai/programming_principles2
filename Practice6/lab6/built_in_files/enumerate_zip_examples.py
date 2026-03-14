# 1
names = ["Akyltai","Karina","Malika","Asan"]
for i,j in enumerate(names):
    print(f'N{i+1} - {j}')
# 2
meals = ["Spagetti","Plov","Borch","Beshparmak"]
for i,j in enumerate(meals):
    print(f'{i}_{j}')
# 3
animals = ["Tiger","Lion","Bird","Eagle"]
for i,j in enumerate(animals):
    print(f'{i}:{j}')
# 4
subject = ["Linear algebra","Calculus","Pp","Physic"]
points = [24.5,21,27,30]
for item in zip(subject,points):
    print(f'{item[0]} - {item[1]}')
# 5
capital = ['Sydney','Amsterdam','Praga','Helsinki']
country = ["Australia","Netherlands","Czech Republic","Finland"]
for items in zip(capital,country):
    print(f'{items[0]} - {items[1]}')