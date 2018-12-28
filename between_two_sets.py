nm = input().split()
n = int(nm[0])
m = int(nm[1])
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
first_max = max(a)
second_min = min(b)
l = []
final = 0
for item in range(first_max,second_min + 1):
    result = [item%first_list_item for first_list_item in a]
    if result.count(0) == len(result):
        l.append(item)
for factor_item in l:
    result = [second_list_item%factor_item for second_list_item in b]
    if result.count(0) == len(result):
        final += 1
print(final)



