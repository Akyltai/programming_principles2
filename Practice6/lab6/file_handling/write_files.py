#1 creare file,write "yo"
with open("new_file.txt",'w') as file:
    file.write("Yo")
#2 create some lines
lines = ["Карина\n","Малика\n","Акылтай\n"]
with open("new_file1.txt",'w',encoding="utf-8") as file:
    file.writelines(lines)
# 3 create file with кирилица
with open("new_file1.txt", "w", encoding="utf-8") as f:
    f.write("Новый файл.")
# # 4 write file with f striing
name = "Python"
with open("info.txt", "w", encoding="utf-8") as f:
    f.write(f"programming language: {name}")
# # 5
with open("save.txt", "w", encoding="utf-8") as f:
    f.write("important data")
    f.flush()