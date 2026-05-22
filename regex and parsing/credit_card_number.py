import re
for _ in range(int(input())):
    c = input()
    v = False
    if bool(re.fullmatch(r"[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}",c)):
        v = True
    if bool(re.search(r"(\d)\1{3,}",''.join(c.split("-")))):
        v = False
    if v:
        print("Valid")
    else:
        print("Invalid")