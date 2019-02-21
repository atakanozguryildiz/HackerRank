nk = input().split()
n = int(nk[0])
k = int(nk[1])
height = list(map(int, input().rstrip().split()))
result = 0 if k > max(height) else max(height) - k 
print(result)
