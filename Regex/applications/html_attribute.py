import re
import sys

n = int(input())
html = sys.stdin.read()

tags = {}

for tag, attrs in re.findall(r'<(\w+)([^<>]*)>', html):
    if tag not in tags:
        tags[tag] = set()

    for attr in re.findall(r'([a-z]+)\s*=[\"\']', attrs):
        tags[tag].add(attr)

for tag in sorted(tags):
    print(f"{tag}:{','.join(sorted(tags[tag]))}")