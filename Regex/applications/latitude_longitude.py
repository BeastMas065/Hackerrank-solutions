import re
r = r'\([+-]?(90(\.0+)?|[0-8]?\d(\.\d+)?), [+-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|[0-9]?\d(\.\d+)?)\)'
for _ in range(int(input())):
    print("Valid" if re.fullmatch(r,input()) else "Invalid")