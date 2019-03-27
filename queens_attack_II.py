nk = input().split()
n = int(nk[0])
k = int(nk[1])
r_qC_q = input().split()
r_q = int(r_qC_q[0])
c_q = int(r_qC_q[1])
indexed_row_obstacles = {}
indexed_column_obstacles = {}

for _ in range(k):
    item = list(map(int, input().rstrip().split()))
    r = item[0]
    c = item[1]
    if r in indexed_row_obstacles:
        columns = indexed_row_obstacles[r]
        columns.append(c)
        indexed_row_obstacles[r] = columns
    else:
        indexed_row_obstacles[r] = [c]
    
    if c in indexed_column_obstacles:
        rows = indexed_column_obstacles[c]
        rows.append(r)
        indexed_column_obstacles[c] = rows
    else:
        indexed_column_obstacles[c] = [r]
    
    

MIN_LIMIT = 1
MAX_LIMIT = n
move = 0
# Directions ; up - down - left - right - upleft - upright
# downleft - downright

# Up
same_column_up_items = list(filter(lambda x: x > r_q,
    indexed_column_obstacles.get(c_q, [])))
if len(same_column_up_items) > 0:
    min_obstacle_row = min(same_column_up_items)
    up_possible_attack_count = min_obstacle_row - r_q - 1
    move += up_possible_attack_count
else:
    up_possible_attack_count = n - r_q
    move += up_possible_attack_count

# Down
same_column_down_items = list(filter(lambda x:x < r_q, indexed_column_obstacles.get(c_q, [])))
if len(same_column_down_items) > 0:
    max_obstacle_row = max(same_column_down_items)
    down_possible_attack_count = r_q - max_obstacle_row - 1
    move += down_possible_attack_count
else:
    down_possible_attack_count = r_q - 1
    move += down_possible_attack_count


# Left
same_row_left_items = list(filter(lambda x: x < c_q, indexed_row_obstacles.get(r_q, [])))
if len(same_row_left_items) > 0:
    max_obstacle_column = max(same_row_left_items)
    left_possible_attack_count = c_q - max_obstacle_column - 1
    move += left_possible_attack_count
else:
    left_possible_attack_count = c_q - 1
    move += left_possible_attack_count



# Right
same_row_right_items = list(filter(lambda x: x > c_q, indexed_row_obstacles.get(r_q, [])))
if len(same_row_right_items) > 0:
    min_obstacle_column = min(same_row_right_items)
    right_possible_attack_count = min_obstacle_column - c_q - 1
    move += right_possible_attack_count
else:
    right_possible_attack_count = n - c_q
    move += right_possible_attack_count

# Diagonals
# Upleft
temp_q_row = r_q
temp_q_column = c_q
while temp_q_row < MAX_LIMIT and temp_q_column > MIN_LIMIT:
    temp_q_row += 1
    temp_q_column -= 1
    columns = indexed_row_obstacles.get(temp_q_row, [])
    if temp_q_column in columns:
        break
    else:
        move += 1

# Upright
temp_q_row = r_q
temp_q_column = c_q
while temp_q_row < MAX_LIMIT and temp_q_column < MAX_LIMIT:
    temp_q_row += 1
    temp_q_column += 1
    columns = indexed_row_obstacles.get(temp_q_row, [])
    if temp_q_column in columns:
        break
    else:
        move += 1

# Downleft
temp_q_row = r_q
temp_q_column = c_q
while temp_q_row > MIN_LIMIT and temp_q_column > MIN_LIMIT:
    temp_q_row -= 1
    temp_q_column -= 1
    columns = indexed_row_obstacles.get(temp_q_row, [])
    if temp_q_column in columns:
        break
    else:
        move += 1

# Downright
temp_q_row = r_q
temp_q_column = c_q
while temp_q_row > MIN_LIMIT and temp_q_column < MAX_LIMIT:
    temp_q_row -= 1
    temp_q_column += 1
    columns = indexed_row_obstacles.get(temp_q_row, [])
    if temp_q_column in columns:
        break
    else:
        move += 1
print(move)
