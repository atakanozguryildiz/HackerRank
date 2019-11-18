#!/bin/python3

n = int(input())
a = list(map(int, input().rstrip().split()))
indices = {}
for i in range(len(a)):
    item = a[i]
    if item in indices:
        item_indice = indices[item].append(i)
    else:
        indices[item] = [i]
indexes = list(filter(lambda k:len(indices[k])>1, indices))
min_val = 999999
for k in indexes:
    item_indexes = indices[k]
    item_min = 999999
    last_index = -1
    for item_index in item_indexes:
        if last_index == -1:
            last_index = item_index
            continue
        temp_index = item_index - last_index
        if temp_index < item_min:
            item_min = temp_index
    if item_min < min_val:
        min_val = item_min
if min_val == 999999:
    print(-1)
else:
    print(min_val)


