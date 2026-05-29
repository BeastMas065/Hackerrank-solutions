import re
r = r"(\d+)([- ])(\d{1,3})\2(\d{4,10})"
for _ in range(int(input())):
    phone = input()
    p = re.finditer(r,phone)
    for m in p:
        print(f'CountryCode={m[1]},LocalAreaCode={m[3]},Number={m[4]}')
    