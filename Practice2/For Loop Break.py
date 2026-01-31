#1
lst = [1,3,4,56,7,6,64,87,5,94,34,8]
find = 5
for i in lst:
    if find == i:
        break
    print(i,end=" ")
#2
friends = ["Asan","Malika","Karina"]
for i in friends:
    if i == "Malika":
        break
    else:
        print("Dude..")
    print(i)
#3
capitals = ["Budapesht","Sidney","Praga","Ankara"]
for i in capitals:
    if i == "Shanhay": #Won't work
        print("It's China!")
        break
    else:
        print("It's other country!")
#4
ing = ["potato","carrot","cucumber","bread"]
for i in ing:
    if i == "bread":
        print("I found bread!")
        break
    else:
        print("Oh,it's not bread :/ ")
#5
Animals = ["Pantera","Lion","Raven","Wolf"]
for i in Animals:
    if i == "Raven":
        print("I afraid Raven!I'm about to run!")
        break
    else:
        print("It's just animal,phh!")