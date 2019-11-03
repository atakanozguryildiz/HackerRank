#!/bin/python3

nd = input().split()
n = int(nd[0])
d = int(nd[1])
arr = list(map(int, input().rstrip().split()))
count = 0
for i in range(len(arr)-2):
    first_item = arr[i]
    second_item = first_item + d
    second_item_check_array = arr[i+1:len(arr)-1]
    if second_item not in second_item_check_array:
        continue
    second_item_count = second_item_check_array.count(second_item)
    second_indexes = []
    last_start = i+1
    for j in range(second_item_count):
        index = arr.index(second_item, last_start, len(arr)-1)
        second_indexes.append(index)
        last_start = index + 1
    for second_index in second_indexes:
        third_item = arr[second_index] + d
        third_item_check_array = arr[second_index:]
        if third_item not in third_item_check_array:
            continue
        second_item_count = third_item_check_array.count(third_item)
        count += second_item_count
print(count)
