from itertools import product
k, m = map(int, input().split())
l = []
for i in range(k):
    arr = list(map(int, input().split()))
    l.append(arr[1:])  
maximum = 0
for values in product(*l):
    total = sum(x**2 for x in values) % m
    maximum = max(maximum, total)
print(maximum)