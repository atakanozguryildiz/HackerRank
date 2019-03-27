nm = input().split()
n = int(nm[0])
m = int(nm[1])
indexes = []
d1 = time.time()
for _ in range(n):
    t = input()
    att_indexes = []
    for i, v in enumerate(t):
        if v == '1':
            att_indexes.append(i)
    indexes.append(att_indexes)

max_count = 0
elem_count = 0
for i, v1 in enumerate(indexes):
    others = indexes[i+1:]
    for v2 in others:
        total = []
        total.extend(v1)
        total.extend(v2)
        total = set(total)
        total_len = len(total)
        if total_len > max_count:
            max_count = total_len
            elem_count = 1
        elif total_len == max_count:
            elem_count += 1
print(max_count)
print(elem_count)
