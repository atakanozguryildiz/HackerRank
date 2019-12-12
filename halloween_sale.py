#!/bin/python3
pdms = input().split()
p = int(pdms[0])
d = int(pdms[1])
m = int(pdms[2])
s = int(pdms[3])

count = 0
is_fixed = False
while(s>=p):
    count += 1
    s -= p
    if not is_fixed:
        temp_p = p - d
        if temp_p < m:
            p = m
            is_fixed = True
        else:
            p -= d
print(count)
