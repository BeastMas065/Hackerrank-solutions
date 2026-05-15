# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
a = input().split()
c = list(itertools.permutations(a[0],int(a[1])))
c = sorted(c)
for i in c:
    print(''.join(i))
