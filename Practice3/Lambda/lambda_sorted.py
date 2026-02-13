#1 только чётные
nums = [4,5,6,7,9,10,2]
srted = sorted(nums,key=lambda x:(x%2==1,x))
print(srted)
#2
Gpa_list = {
    "Akyltai":4.000,
    "Someone":2.900,
    "Karina":3.990,
    "Malika":3.998
}
gpa_sort = sorted(Gpa_list,key=lambda x:x[0])
print(gpa_sort)
#3
names = ["Anuar","Asylkhan","Danyar","Alfarabi","Karina"]
sort_by_last_letter = sorted(names,key=lambda x:x[-1].lower())
print(sort_by_last_letter)
#4
numbers = [1,2,3,-9,-4,-5,0]
sort_by_abs = sorted(numbers,key=lambda x: abs(x))
print(sort_by_abs)
#5
prices = ["Banana-700","strawberry-600","Sugar-200"]
sort_by_price = sorted(prices,key=lambda x: int(x.split("-")[1]))
print(sort_by_price)