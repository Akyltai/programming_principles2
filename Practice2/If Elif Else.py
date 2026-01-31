#1
a = int(input(":"))
if a%2 == 0:
    print("It's even num")
elif a%2 != 0:
    print("It's even num")
else:
    print("Error!Please try again!")
#2
certificate = True
age = int(input("Input your age:"))
if age>18:
    print("U can go in")
elif age>=18 and certificate:
    print("U can go in")
else:
    print("Get out!")
#3
score = int(input(":"))
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=50:
    print("D")
else:
    print("Retake")
#4
rain_today = False
sunny = True 
temp = int(input(":"))
if rain_today:
    if temp<15 and temp>10:
        print("Dress warmer")
elif sunny:
    if temp>25 and temp<40:
        print("Put on a T-short and shorts")
else:
    print("Haven't enough data")

#5
wei = int(input("Your weidth:"))
hei = int(input("Your height:"))
BMI = float(wei/hei)
if BMI<18.5:
    print("Underweidth")
elif 18.5 <= BMI <25:
    print("It's good!normal weidth")
elif 25<=BMI <30:
    print("Ohh,onverweidth")
else:
    print("Obesity")