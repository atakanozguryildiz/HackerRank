q = int(input())
for q_itr in range(q):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    count = 0
    start_point = int(a ** 0.5)
    end_point = int(b ** 0.5)
    r = range(a, b+1)
    count = 0
    for i in range(start_point, end_point+1):
        if i ** 2 in r:
            count += 1
    print(count)
