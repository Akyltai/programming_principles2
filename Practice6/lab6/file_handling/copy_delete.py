import shutil
import os
#1 holder delete
import shutil
shutil.rmtree("folder_to_delete")
#2 copy,then delete file
shutil.move("new_file1.txt", "new_file2.txt")
# 3 copy file
shutil.copy("new_file1.txt","new_file.txt")
print("File succesfully copied")
# 4 remove file
if os.path.exists("new_file1.txt"):
    os.remove("new_file1.txt")
    print("'new_file1.txt' was removed")
#5 copy holder
shutil.copytree("my_folder", "backup_folder")