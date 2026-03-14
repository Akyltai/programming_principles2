s = input()
vowels = "aeiou"
if any(char.lower() in vowels for char in s):
    print("Yes")
else:
    print("No")