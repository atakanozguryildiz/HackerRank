n = int(input().strip())
a = list(map(int, input().rstrip().split()))
each_elements = set(a)
max_count = 0
for i in each_elements:
    arr_elements = [[i, i+1], [i, i-1]]
    for j in arr_elements:
        temp_total = 0
        for z in j:
            temp_total += a.count(z)
        if temp_total > max_count:
            max_count = temp_total
print(max_count)
