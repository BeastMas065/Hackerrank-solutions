# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
a = set(list(map(int,input().split())))
f = int(input())
b = set(list(map(int,input().split())))

o = a.union(b)
print(len(o))