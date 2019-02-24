t = int(input())
for t_itr in range(t):
    n = int(input())
    count = 0
    for i in str(n):
        if int(i) == 0:
            continue
        if n % int(i) == 0:
            count += 1
    print(count)
