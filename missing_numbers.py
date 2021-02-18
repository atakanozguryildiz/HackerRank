n = int(input())
arr = list(map(int, input().rstrip().split()))
m = int(input())
brr = list(map(int, input().rstrip().split()))
number_time = dict()
second_number_time = dict()
for i in arr:
    if i in number_time:
        number_time[i] = number_time[i] + 1
    else:
        number_time[i] = 1
for i in brr:
    if i in second_number_time:
        second_number_time[i] = second_number_time[i] + 1
    else:
        second_number_time[i] = 1

missings = set()
for i in second_number_time:
    if i not in number_time:
        missings.add(i)
        continue
    n_t = number_time[i]
    s_t = second_number_time[i]
    if s_t != n_t:
        missings.add(i)
sorted_missings = list(map(lambda x:str(x), sorted(missings)))
print(" ".join(sorted_missings))