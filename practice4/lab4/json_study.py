import json
# #1
# json_str='{"name": "Busia", "age": 5, "is_hungry": true, "color": "ginger"}'
# data = json.loads(json_str)
# print(f"{data['name']} is {data['age']} years old and is {data['color']} color")
# if data['is_hungry']:
#     print("let's go feed")
# #2
# json_students = '''
# [
#     {"name": "Alice", "GPA": 3.23},
#     {"name": "Bob", "GPA": 2.11},
#     {"name": "Charlie", "GPA": 3.55},
#     {"name": "Diana", "GPA": 4.00}
# ]
# '''
# info = json.loads(json_students)
# for student in info:
#     if student['GPA']<3.5:
#         print(f"{student['name']} get retake!")
# #3
# json_iss = '''
# {
#     "status": "success",
#     "data": {
#         "station_name": "ISS",
#         "location": {"lat": 45.12, "lon": -120.45},
#         "crew": ["Oleg", "Jessica", "Hans"]
#     }
# }
# '''
# data_info = json.loads(json_iss)
# print(f"Station name is {data_info['data']['station_name']}. It's located in {data_info['data']['location']['lat']}")
# for i,member in enumerate(data_info['data']['crew']):
#     print(f"Station number {i} - {member}")
# #4
# def create_user(n):
#     arr = []
#     for _ in range(n):
#         name = input()
#         age = int(input())
#         skills = input().split()
#         dict = {
#             "name":name,
#             'age':age,
#             'skills':skills
#         }
#         arr.append(dict)
#     return json.dumps(arr,indent=4,ensure_ascii=False)
# n = int(input())
# print(create_user(n))
# #5
def choose_book(n):
    lst = []
    for _ in range(n):
        name = input()
        author = input()
        dict = {'name':name,'author':author}
        lst.append(dict)
    return json.dumps(lst,sort_keys=True,indent=4)
print(choose_book(3))