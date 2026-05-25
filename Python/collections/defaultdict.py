from collections import *
n, m = map(int,input().split())
a = defaultdict(list)
b = []
for i in range(1,n+1):
    c = input()
    a[c].append(i)
for i in range(m):
    b.append(input())
for i in b:
    if i in a:
        print(' '.join(map(str,a[i])))
    else:
        print('-1')