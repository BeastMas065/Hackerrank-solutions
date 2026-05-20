s = input()
x = [x for x in s if x.isupper()]
y = [x for x in s if x.islower()]
z = [int(x) for x in s if x.isdigit()]
p = [x for x in z if x%2==0]
q = [x for x in z if x%2!=0]
x = sorted(x)
y = sorted(y)
p = list(map(str,sorted(p)))
q = list(map(str,sorted(q)))
s = y+x+q+p
print(''.join(s))