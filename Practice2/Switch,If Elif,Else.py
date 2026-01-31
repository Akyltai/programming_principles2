#1
day = int(input())

match day:
    case 1|2|3|4|5:
        print("Work day")
    case 6|7:
        print("Holidays")
    case _:
        print("Error")
#2
grade = int(input("Enter your grade (1-5): "))

match grade:
    case 5:
        print("Excellent!")
    case 4:
        print("Good job")
    case 3:
        print("Satisfactory")
    case 1 | 2:
        print("Retake required")
    case _:
        print("Unknown grade")
#3
a = int(input(":"))
b = int(input(":"))
action = input("Enter operation (+, -, *, /): ")

match action:
    case "+":
        print(f"Result: {a + b}")
    case "-":
        print(f"Result: {a - b}")
    case "*":
        print(f"Result: {a * b}")
    case "/":
        print(f"Result: {a / b}")
    case _:
        print("Operation not supported")
#4
time = input("Is it morning, afternoon, or evening? ").lower()

match time:
    case "morning":
        print("Good morning!")
    case "afternoon":
        print("Good afternoon!")
    case "evening":
        print("Good evening!")
    case _:
        print("Hello!")
#5
distance = input("How far is it? (short/medium/long): ").lower()

match distance:
    case "short":
        print("Walk there.")
    case "medium":
        print("Take a bike.")
    case "long":
        print("You need a car or bus.")
    case _:
        print("Distance unknown.")