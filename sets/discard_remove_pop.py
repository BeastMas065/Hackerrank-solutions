n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    a = input().split()
    if a[0][0] == 'p':
        s.pop()
    elif a[0][0] == 'r':
        s.remove(int(a[1]))
    else:
        s.discard(int(a[1]))
sum = 0
for i in s:
    sum += i
print(sum)
