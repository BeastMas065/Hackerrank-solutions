import re
l=[]
for _ in range(int(input())):
    n=input()
    m=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",n)
    l.extend(m)
print(";".join(sorted(set(l))))