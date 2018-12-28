nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
divisible_count = 0
for i in range(n):
    sub_ar = ar[i+1:n]
    elem = ar[i]
    totals = list(map(lambda x:x+elem, sub_ar))
    divisible_count += len(list(filter(lambda x:x%k==0,totals)))
print(divisible_count)

