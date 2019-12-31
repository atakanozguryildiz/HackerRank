#!/bin/python3

t = int(input())
for t_itr in range(t):
    ncm = input().split()
    n = int(ncm[0])
    c = int(ncm[1])
    m = int(ncm[2])
    count = 0
    wrapper = 0
    while n >= c:
        n -= c
        wrapper += 1
        count += 1
    while wrapper >= m:
        wrapper -= m
        count += 1
        wrapper += 1
    print(count)
