import itertools
s,k = input().split()
for i in range(1,int(k)+1):
    c = list(itertools.combinations(sorted(s),i))
    for j in c:
        print(''.join(j))