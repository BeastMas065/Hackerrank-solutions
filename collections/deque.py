from collections import *
l = deque()
for i in range(int(input())):
    cmd,*a = input().split()
    getattr(l,cmd)(*a)
print(*l)