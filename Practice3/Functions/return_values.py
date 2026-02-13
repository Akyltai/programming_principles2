#1
n1 = int(input())
n2 = int(input())

def sum(n1,n2):
    return n1+n2
print(sum(n1,n2))
#2
def check_age(age):
    if age<0:
        return "Age cannot be negative"
    return "Vallid data"
print(check_age(3))
#3
def get_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum # Возвращает кортеж (min, max)

low, high = get_min_max([10, 2, 45, 1])
print(f"Min: {low}, Max: {high}")
# 4
def is_odd(nums):
    if nums%2 == 0:
        return "Nope"
    elif nums%2 != 0:
        return "Yep"
    else:
        return "Error"
print(is_odd(8))
#5
def find_first_negative_nums(lst):
    for i in lst:
        if i<0:
            return i
lst = [9,0,4,3,5,-9,3,2,4,5,6,7,-8]
print(find_first_negative_nums(lst))