# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(list(map(int,input().split())))
N = int(input())
for i in range(N):
    p = input().split()
    q = set(map(int,input().split()))
    if p[0] == "update":
        a.update(q)
    if p[0] == "intersection_update":
        a.intersection_update(q)
    if p[0] == "difference_update":
        a.difference_update(q)
    if p[0] == "symmetric_difference_update":
        a.symmetric_difference_update(q)
print(sum(a))