#1
number = 0
limit = int(input(":"))
while number < limit:
    number += 1
    if number % 2 == 0:
        continue 
    print("Odd number:", number)
# 2
floor = 0
while floor < 5:
    floor += 1
    if floor == 4: #Fourth floor don't work
        continue
    print("Elevator reached floor:", floor)
# 3
balance = int(input(":"))
while balance > -5:
    balance -= 1
    if balance < 0:
        print("Negative value found, skipping calculation.")
        continue
    print("Processing balance:", balance)
# 4
while True:
    username = input("Create username (min 5 chars): ")
    if len(username) < 5:
        print("Too short! Try again.")
        continue
    
    print("Username accepted:", username)
    break
#5
data = ["Akyltai", "", "Asanhan", "Karina", "","Malika"]
index = 0

while index < len(data):
    entry = data[index]
    index += 1 
    
    if entry == "":
        continue
        
    print("Valid entry found:", entry)