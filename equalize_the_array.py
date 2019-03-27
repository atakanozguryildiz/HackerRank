nt(input())
arr = list(map(int, input().rstrip().split()))

elems = {}
max_elem = -1
max_count = -1
for i in arr:
    if i in elems:
        c = elems[i]
        elems[i] = c + 1
        if c + 1 > max_count:
            max_count = c + 1
            max_elem = i
    else:
        elems[i] = 1
        if 1 > max_count:
            max_count = 1
            max_elem = i
print(len(arr) - max_count)
