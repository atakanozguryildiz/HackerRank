#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    if not isinstance(a, list) or not isinstance(b, list) or len(a) != len(b):
        raise ValueError("`a` and `b` arguments must be list and equal length")

    total_length = len(a)
    point_a = 0
    point_b = 0
    for i in range(0, total_length):
        item_a = a[i]
        item_b = b[i]
        if 1 <= item_a <= 100 and 1 <= item_b <= 100:
            if item_a > item_b:
                point_a += 1
            elif item_b > item_a:
                point_b += 1
                
    return [point_a, point_b]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
