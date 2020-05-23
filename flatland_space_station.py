nm = input().split()
n = int(nm[0])
m = int(nm[1])
space_indexes = list(map(int, input().rstrip().split()))

space_indexes = sorted(space_indexes)
result = 0

result = space_indexes[0]
last_index = n - 1
last_space_index = space_indexes[len(space_indexes) - 1]
last_diff = abs(last_space_index - last_index)
if last_diff > result:
    result = last_diff

for i, space_index in enumerate(space_indexes):
    if i == len(space_indexes) - 1:
        break
    next_space_index = space_indexes[i + 1]
    diff = next_space_index - space_index
    if diff == 1:
        continue
    dist = diff / 2
    if dist > result:
        result = int(dist)
print(result)