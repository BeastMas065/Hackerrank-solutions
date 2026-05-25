# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int,input().split()))
n = int(input())
b = set(map(int,input().split()))
c = a.symmetric_difference(b)
c = sorted(list(c))
for i in c:
    print(i)