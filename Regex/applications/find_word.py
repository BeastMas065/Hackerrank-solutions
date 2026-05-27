import re
para = ''
for _ in range(int(input())):
    para += input() + '\n'
for _ in range(int(input())):
    t = input()
    fe = re.findall(rf'\b{t}\b',para)
    print(len(fe))