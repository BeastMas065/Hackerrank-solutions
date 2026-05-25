# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
n = int(input())
l = OrderedDict()
for i in range(n):
    p = input().split()
    item = ' '.join(p[:-1])
    if item in l:
        l[item] += int(p[-1])
    else:
        l[item] = int(p[-1])    
for k,v in l.items():
    print(k,v)