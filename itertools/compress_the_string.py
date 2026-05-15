import itertools
s = input()
for k, g in itertools.groupby(s):
    print((len(list(g)),int(k)),end=' ') 