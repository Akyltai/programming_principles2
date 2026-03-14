import os
# 1 find abcolute path
file_name = "example2.txt"
full_path = os.path.abspath(file_name)
# 2 rename file name
if os.path.exists("example2.txt"):
    os.rename("old_name.txt", "new_name.txt")
# 3 found dile size
file_size = os.path.getsize("example.txt")
# 4 found files without holder
for item in os.listdir('.'):
    if os.path.isfile(item):
        print(f"Found file: {item}")
    else:
        print(f"It is: {item}")
# 5 remove dire
os.rmdir('new_folder')