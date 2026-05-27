import re
import sys

html = sys.stdin.read()

pattern=r'href=\"([^-]*?)\"[^>]*>(<[^>]*>)?\s?([^>]*?)<'

matches = re.findall(pattern, html)

for match in matches:
    print(",".join((match[0], match[2])))