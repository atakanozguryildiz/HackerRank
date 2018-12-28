n = int(input())
scores = list(map(int, input().rstrip().split()))
user_max = scores[0]
user_min = scores[0]
max_break_count = 0
min_break_count = 0
for score in scores:
    if score < user_min:
        user_min = score
        min_break_count += 1
    elif score > user_max:
        user_max = score
        max_break_count += 1
print(max_break_count, min_break_count, sep=" ")



