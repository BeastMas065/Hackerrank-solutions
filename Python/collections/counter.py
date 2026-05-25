from collections import Counter
x = int(input())
sizes = list(map(int,input().split()))
n = int(input())
c = Counter(sizes)
total = 0
for i in range(n):
    size, price = map(int,input().split())
    if c[size] > 0:
        total += price
        c[size] -= 1
print(total)