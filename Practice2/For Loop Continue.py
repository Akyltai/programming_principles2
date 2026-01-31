#1
nums = [1,2,3,4,5,6,7,8,9,10]
for i in nums:
    if i%2 == 0:
        continue
    print(i,end=" ")
#2
gpa={
    1:3.27,
    2:4.0,
    3:2.7,
    4:1.8,
    5:2.2,
    6:2.5,
    7:1.2
}
print("Numbers of people who take a retake:")
for i in gpa.keys():
    if gpa[i] >= 2.7:
        continue
    print(f"Student ID {i} (GPA : {gpa[i]})")
#3
for_meal = []
products = ['potato','onions','carrot','olive','cabbage','eggplants']
print("I have: ",end=" ")
print(*(products))
for ingredients in products:
    if ingredients == 'olive':
        print("bee,I don't like olives!!")
        continue #I don't like olive
    for_meal.append(ingredients)
print("For meal I want use:")
print(*(for_meal),end=" ")
#4
music_genre = ('pop','rock','hip-hop','rap','jazz','folk')
for index,genre in enumerate(music_genre):
    if genre[0] != 'r':
        continue
    print(f"My favorite genre under number {index} is {genre}")
#5
names = "Asan Karina Akyltai Malika Ali"
name = list(names.split())
for bests in name:
    if len(bests)<4:
        print(f"Retake for {bests}!")
        continue
    print(f"{bests} is a best KBTU student!")