#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    common = 0

    while common < min(len(s), len(t)) and s[common] == t[common]:
        common += 1

    operations = (len(s) - common) + (len(t) - common)

    if operations > k:
        return "No"
    elif (k - operations) % 2 == 0:
        return "Yes"
    elif k >= len(s) + len(t):
        return "Yes"
    else:
        return "No"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
