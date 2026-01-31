#1
n = 0
while True:
    print(n)
    n+=1
    if n == 5:
        break
#2
secret_password = "Akyltai"
while True:
    guess = input("Enter password: ")
    if guess == secret_password:
        print("Access granted.")
        break
    print("Wrong password, try again.")
#3
number = 1
target = 7

while number <= 20:
    if number == target:
        print("Target found: ", number)
        break
    number += 1
#4
temperature = int(input(":"))

while temperature < 100:
    print("Current temperature:", temperature)
    if temperature >= 50:
        print("Safety limit reached. Shutting down.")
        break
    temperature += 10
#5
total_sum = 0
count = 1

while count <= 100:
    total_sum += count
    if total_sum > 50:
        print("Sum limit exceeded at:", total_sum)
        break
    count += 1