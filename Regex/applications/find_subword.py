import re
sentence = ''
for _ in range(int(input())):
    sentence += input() + '\n'
for _ in range(int(input())):
    s = input()
    p = re.findall(rf'\w{s}\w',sentence)
    print(len(p))