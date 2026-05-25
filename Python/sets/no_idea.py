happy = 0
(n , m) = map(int, input().split())
arr = list(map(int,input().split()))
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))
for x in arr:
    if x in a:
        happy += 1
    elif x in b:
        happy -= 1
    else:
        pass
print(happy)