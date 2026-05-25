import re

s = input()
k = input()

m = re.finditer(r'(?={})'.format(re.escape(k)), s)

found = False

for i in m:
    print((i.start(), i.start() + len(k) - 1))
    found = True

if not found:
    print((-1, -1))