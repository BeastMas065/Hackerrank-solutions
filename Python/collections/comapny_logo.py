from collections import Counter

s = input()

c = Counter(s)

l = sorted(c.items(), key=lambda x: (-x[1], x[0]))

for a, b in l[:3]:
    print(a, b)