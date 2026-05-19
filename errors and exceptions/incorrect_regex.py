import re

for _ in range(int(input())):
    s = input()

    if re.search(r'(\*\+|\+\+|\?\+)', s):
        print(False)
        continue

    try:
        re.compile(s)
        print(True)
    except re.error:
        print(False)