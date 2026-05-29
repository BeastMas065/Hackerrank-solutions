import sys
import re

code = sys.stdin.read()

pattern = r'//.+|/\*[\s\S]+?\*/'
for comment in re.findall(pattern,code):
    if comment.startswith('/*'):
        #comment = ("\n".join([x.strip() for x in re.split(r'\n',comment)]))
        comment = re.split(r'\n',comment)
        for line in comment:
            print(line.strip())
    
    else:
        print(comment)