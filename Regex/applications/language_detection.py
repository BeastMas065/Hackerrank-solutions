import re
import sys
code = sys.stdin.read()
c = r'\(\)\s\{'
j = r'java\.io'
if re.search(j,code):
    print('Java')
elif re.search(c,code):
    print('C')
else:
    print('Python')