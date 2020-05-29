#!/bin/python3

N = int(input())
B = list(map(int, input().rstrip().split()))

starter_index = 0
counter = 0

unsuccess = False
for index, item in enumerate(B):
    if index == len(B) - 1:
        if item % 2 == 0:
            break
        else:
            unsuccess = True
            break
    if item % 2 == 1:
        next_item = B[index + 1]
        B[index] = item + 1
        B[index + 1] = B[index + 1] + 1
        counter += 2

if unsuccess:
    print("NO")
else:
    print(counter)