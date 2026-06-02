#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    P = 0
    N = 0
    Z = 0
    for i in range(n):
        if arr[i]>0:
            P += 1
        elif arr[i]<0:
            N += 1
        else:
            Z += 1
    P = P/n
    N = N/n
    Z = Z/n
    print(f'{P:.6f}')        
    print(f'{N:.6f}')        
    print(f'{Z:.6f}')        


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
