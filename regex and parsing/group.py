import re
m = re.search(r'([A-Za-z1-9])\1+',input())
try:
    print(m.group(1))
except AttributeError:
    print("-1")