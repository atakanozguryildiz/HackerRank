n = int(input())
c = list(map(int, input().rstrip().split()))
current_pos = 0
max_pos = len(c) - 1
move_count = 0
while current_pos != max_pos:
    moves = [2, 1]
    for move in moves:
        temp_pos = move + current_pos
        if temp_pos > max_pos:
            continue
        temp_i = c[temp_pos]
        if temp_i == 1:
            continue
        current_pos = temp_pos
        move_count += 1
        break
print(move_count)
