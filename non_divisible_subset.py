nk = input().split()
n = int(nk[0])
k = int(nk[1])
S = list(map(int, input().rstrip().split()))

r = [0 for _ in range(k)]
for s in S:
    r[s%k] += 1

if k % 2 == 0:
    half_index = int(k/2)
    r[half_index] = min(r[half_index], 1)

res = min(r[0], 1)
for i in range(1, k//2 + 1):
    res += max(r[i], r[k-i])
print(res)
