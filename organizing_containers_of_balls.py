q = int(input())
for q_itr in range(q):
    n = int(input())
    container = []
    is_possible = True
    for _ in range(n):
        container.append(list(map(int, input().rstrip().split())))
    count = len(container)
    container_elem_counts = []
    ball_elem_counts = []
    con_elem_indexes = {}
    for i in range(0, count):
        con_elem_indexes[i] = 0
    for con in container:
        con_elem_count = sum(con)
        container_elem_counts.append(con_elem_count)
        for i, v in enumerate(con):
            elem_count = con_elem_indexes[i]
            elem_count += v
            con_elem_indexes[i] = elem_count
    ball_elem_count = list(con_elem_indexes.values())
    c_sorted = sorted(container_elem_counts)
    b_sorted = sorted(ball_elem_count)
    if c_sorted == b_sorted:
        print('Possible')
    else:
        print('Impossible')

