ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
count = 0
for day in range(i, j+1):
    reverse = int(str(day)[::-1])
    dif = abs(day-reverse)
    if dif % k == 0:
        count += 1
print(count)

