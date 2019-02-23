t = int(input())
for t_itr in range(t):
    nms = input().split()
    n = int(nms[0])
    m = int(nms[1])
    s = int(nms[2])
    if m > n:
        mod = m % n
        m = mod if mod != 0 else n
    result = s - 1 + m
    while(result > n):
        result -= n
    print(result)
