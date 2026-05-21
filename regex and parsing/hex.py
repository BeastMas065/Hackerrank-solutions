import re

for _ in range(int(input())):
    line = input()
    if ':' in line:
        matches = re.findall(r'(?i)#[0-9a-f]{6}|#[0-9a-f]{3}',line)
        for m in matches:
            print(m)