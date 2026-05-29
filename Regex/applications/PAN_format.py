import re
r = r'[A-Z]{5}\d{4}[A-Z]'
for _ in range(int(input())):
    s = input()
    if re.fullmatch(r,s):
        print("YES")
    else:
        print("NO")