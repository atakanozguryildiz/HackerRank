ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
max_height = 0
max_count = 0
for i in ar:
    if i > max_height:
    	max_height = i
    	max_count = 1 
    elif i == max_height:
    	max_count += 1
print(max_count)

