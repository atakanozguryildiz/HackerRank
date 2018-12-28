arr = list(map(int, input().rstrip().split()))
sorted_arr = sorted(arr)
min_items = sorted_arr[:-1]
max_items = sorted_arr[1:]
total_min = sum(min_items)
total_max = sum(max_items)
print ("{} {}".format(total_min, total_max))


