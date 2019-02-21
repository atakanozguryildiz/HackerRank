t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    arrived_at_time = len(list(filter(lambda x:x<=0, a)))
    if arrived_at_time >= k:
        print("NO")
    else:
        print("YES")
