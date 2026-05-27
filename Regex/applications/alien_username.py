import re
for _ in range(int(input())):
    print("VALID" if bool(re.fullmatch(r'[_.][0-9]+[a-zA-Z]*_?',input())) else "INVALID")