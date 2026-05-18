from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    l = deque(list(map(int,input().split())))
    high = float("inf")
    while l:
        if l[0] >= l[-1]:
            x = l.popleft()
        else:
            x = l.pop()
        if x > high:
            print("No")
            break
        high = x
    if l == deque([]):
        print("Yes")