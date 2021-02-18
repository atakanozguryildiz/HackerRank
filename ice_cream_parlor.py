t = int(input())
for t_itr in range(t):
    m = int(input())
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            f = arr[i]
            s = arr[j]
            if s + f != m:
                continue
            print(i+1, j+1, " ")