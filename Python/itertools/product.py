# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(itertools.product(a,b))
for i in c:
    print(i,end=' ')