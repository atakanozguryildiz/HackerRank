#!/bin/python3

import math
import os
import random
import re
import sys

s = input()
n = int(input())

count = 0
for i in s:
    if i == 'a':
        count += 1

s_count = n // len(s)
count *= s_count
if n % len(s) != 0:
    remain = n% len(s)
    remain_s = s[:remain]
    for i in remain_s:
        if i == 'a':
            count += 1
print(count)
