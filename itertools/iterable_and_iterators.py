# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
n = int(input())
s = input().split()
k = int(input())
total = 0
withk = 0
for i in itertools.combinations(s,int(k)):
    total += 1
    if 'a' in i:
        withk += 1
p = withk/total
print(f'{p:.3f}')