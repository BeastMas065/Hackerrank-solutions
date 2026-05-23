import numpy as n
a = n.array(list(map(int,input().split())))
b = n.array(list(map(int,input().split())))
print(n.inner(a,b))
print(n.outer(a,b))