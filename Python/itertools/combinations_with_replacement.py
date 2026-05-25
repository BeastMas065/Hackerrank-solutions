# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
s,k = input().split()
c = list(itertools.combinations_with_replacement(sorted(s),int(k)))
for m in c:
    print(''.join(m))