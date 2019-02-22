n = int(input())
total = 0
start_point = 5
for i in range(n):
    liked = start_point // 2
    total += liked
    start_point = liked * 3
print(total)
