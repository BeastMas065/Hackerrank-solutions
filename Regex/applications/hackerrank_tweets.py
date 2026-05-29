import re
r = r'(?i)hackerrank'
count = 0
for _ in range(int(input())):
    tweet = input()
    if re.search(r,tweet):
        count += 1
print(count)