import os
# 1 get path to directory
print(os.getcwd())
# 2 change directory
os.chdir(r'C:\Users\Админ\Desktop\pp2 labs\Practice6\lab6')
print(os.getcwd())
# 3 make/create dire
os.mkdir('new_folder')
# 4 mare/create some level dire
os.makedirs('first_level/second_level/third_level')
# 5 show all files in path('.' means current directory)
contents = os.listdir('.')
print(contents)