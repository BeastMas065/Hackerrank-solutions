import re
sequence = ''
for _ in range(int(input())):
    sequence += input()
t = int(input())
for _ in range(t):
    count = 0
    word = input()
    mod = word[:-2]+'s'+word[-1]
    p = re.findall(f'{word}|{mod}',sequence)
    print(len(p))