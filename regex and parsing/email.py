import re
for _ in range(int(input())):
    n,e = input().split()
    m = re.fullmatch(r'<[A-Za-z][A-Za-z0-9_.-]*\@[A-Za-z]+\.[A-Za-z]{1,3}>',e)
    if m:
        print(n,e)