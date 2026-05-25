import re

s = input()

m = re.findall(
    r'(?i)(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])',
    s
)

if m:
    for i in m:
        print(i)
else:
    print(-1)