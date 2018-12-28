#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):

    if len(ar) > 10:
        ar = ar[:10]

    limit_min = 0
    limit_max = 10 ** 10
    total = 0
    for i in ar:
        if limit_min <= i <= limit_max:
            total += i
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

