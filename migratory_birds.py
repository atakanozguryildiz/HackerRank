arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
bird_counts = {}
for i in arr:
    item_count = bird_counts.get(i, 0)
    bird_counts[i] = item_count + 1
number_of_most_common_bird = (-1,-1)
for k,v in bird_counts.items():
    n_most_common = number_of_most_common_bird[1]
    if v > n_most_common:
        number_of_most_common_bird = (k, v)
    elif v == n_most_common and k < number_of_most_common_bird[0]:
        number_of_most_common_bird = (k, v)
print(number_of_most_common_bird[0])

