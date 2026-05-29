import re
r = r'(?i)hi (?!d)'
for _ in range(int(input())):
    s = input()
    if re.match(r,s):
        print(s)