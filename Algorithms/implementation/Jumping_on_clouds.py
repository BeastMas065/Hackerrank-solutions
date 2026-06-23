#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    route = []
    pos = 0

    while True:
        pos = (pos + k) % n
        route.append(c[pos])
        if pos == 0:
            break

    count = Counter(route)
    return 100 - (count[0]) - (3 * count[1])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
