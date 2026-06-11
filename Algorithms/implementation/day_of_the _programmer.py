#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    feb = 28
    if year < 1918:
        if year % 4 == 0:
            feb = 29
    elif year  == 1918:
        return("26.09.1918")
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            feb = 29
    days = (5*31) + 60 + feb
    date = 256 - days
    return(f'{date}.09.{year}')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
