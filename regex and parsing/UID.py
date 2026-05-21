import re
for _ in range(int(input())):
    s = input()
    v = True
    if not bool(re.fullmatch(r"[a-zA-Z0-9]{10}", s)):
        v = False
    c = 0
    for ch in s:
        if ch.isdigit():
            c += 1
    if c < 3:
        v = False
    
    if not len(set(s)) == len(s):
        v = False
    if v:
        print("Valid")
    else:
        print("Invalid")