import re
r = r'[a-z]{0,3}\d{2,8}[A-Z]{3}'
for _ in range(int(input())):
    s = input()
    if re.match(r,s):
        print("VALID")
    else:
        print("INVALID")