import re

html = ""
for _ in range(int(input())):
    html += input() + "\n"

pattern = r'https?://(?:www\.|ww2\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'

domains = sorted(set(re.findall(pattern, html)))

print(";".join(domains))