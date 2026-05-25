from collections import *
n = int(input())
l = defaultdict(int)
for i in range(n):
    p = input()
    l[p] += 1
print(len(l.keys()))
for i in l.values():
    print(i,end = ' ')