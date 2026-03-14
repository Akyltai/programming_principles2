from functools import reduce
# 1 map
lst = [2,4,6]
a = list(map(lambda x:x**x,lst))
print(a)
# 2
lst1 = [3,9,27,282,93,4,5]
b = list(filter(lambda x:x%3 == 0,lst1))
print(b)
# 3
a = ["Akyltai", "want", "4.00 GPA"]
r = reduce(lambda x, y: x + "_" + y, a)
print(r)
# 4
nums = ['234','567','789']
c = list(map(int,nums))
for i in c:
    print(f'{i} - {type(i)}')
# 5
lst = [1,2,3]
a = list(map(lambda x:x*3,lst))
print(a)