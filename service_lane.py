#!/bin/python3

nt = input().split()
n = int(nt[0])
t = int(nt[1])
width = list(map(int, input().rstrip().split()))
for _ in range(t):
    case = list(map(int, input().rstrip().split()))
    min_wide = min(width[case[0]: case[1]+1])
    print(min_wide)
