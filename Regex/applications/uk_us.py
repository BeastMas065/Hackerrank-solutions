import re

text = ''
for _ in range(int(input())):
    text += input() + '\n'

for _ in range(int(input())):
    word = input()

    us = word.replace('our', 'or')

    pattern = rf'\b(?:{word}|{us})\b'

    print(len(re.findall(pattern, text)))
