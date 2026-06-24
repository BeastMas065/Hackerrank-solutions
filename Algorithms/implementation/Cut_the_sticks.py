#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import Counter

def cutTheSticks(arr):
    freq = Counter(arr)
    r = []
    length = len(arr)

    for stick_len in sorted(freq):
        r.append(length)
        length -= freq[stick_len]

    return r
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
