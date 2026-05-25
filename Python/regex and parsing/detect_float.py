import re
t = int(input())
for _ in range(t):
    n = input()
    print(bool(re.fullmatch(r'[+-]?\d*\.\d+',n)))