import re
to_num = {
    'ZER':'0', 'ONE':'1', 'TWO':'2', 'THR':'3', 'FOU':'4',
    'FIV':'5', 'SIX':'6', 'SEV':'7', 'EIG':'8', 'NIN':'9'
}
to_word = {v: k for k, v in to_num.items()}
data = input().strip()
sign = re.search(r'[\+\-\*]', data).group()
parts = data.split(sign)
def get_number(text):
    res = ""
    for i in range(0, len(text), 3):
        res += to_num[text[i:i+3]]
    return int(res)

num1 = get_number(parts[0])
num2 = get_number(parts[1])

if sign == '+':   result = num1 + num2
elif sign == '-': result = num1 - num2
else:             result = num1 * num2

final_text = ""
for digit in str(result):
    if digit == '-':
        continue
    final_text += to_word[digit]
print(final_text)