#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    bill = 0
    cell = -1
    keyboards.sort()
    drives.sort()
    for i in range(len(keyboards),0,-1):
        for j in range(len(drives),0,-1):
            if keyboards[i-1]+drives[j-1] <= b:
                cell = keyboards[i-1]+drives[j-1]
                break
        bill = max(cell, bill)
    return bill if bill else cell
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
 