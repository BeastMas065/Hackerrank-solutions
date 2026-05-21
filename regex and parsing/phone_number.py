import re
for _ in range(int(input())):
    b = re.match(r'^[7-9]\d{9}$',input())
    if b:
        print("YES")
    else:
        print("NO")