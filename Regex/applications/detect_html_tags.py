import re
html = ''
for _ in range(int(input())):
    html += input() + '\n'
p = re.findall(r'<(\w+).*?>',html)
all = []
for i in p:
    all.append(i)
all = sorted(list(set(all)))
print(*all,sep=';')