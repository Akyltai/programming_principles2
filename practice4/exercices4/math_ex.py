import math
#1
n = int(input())
radians = math.radians(n)
print(radians)
#2
height = 5
base_1 = 5
base_2 = 6
area_2 = ((base_1 + base_2) / 2) * height
print(area_2)
#3
n_sides = 4
s_length = 25
area_3 = (n_sides * s_length**2) / (4 * math.tan(math.pi / n_sides))
print(int(area_3))
#4
base_length = 5
height = 6
area_4 = float(base_length * height)
print(area_4)