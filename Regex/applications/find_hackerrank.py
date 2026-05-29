import re
r1 = r'hackerrank'
r2 = r'^hackerrank(?!$)'
r3 = r'(?<!^)hackerrank$'
for _ in range(int(input())):
    s = input()
    if re.fullmatch(r1,s):
        print(0)
    elif re.search(r2,s):
        print(1)
    elif re.search(r3,s):
        print(2)
    else:
        print(-1)     