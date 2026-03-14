n = input()
words = set(map(int,(input().split(' '))))
s_lst = sorted(words)
print(*s_lst)