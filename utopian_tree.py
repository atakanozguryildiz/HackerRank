cycles = []
t = int(input())
for t_itr in range(t):
    n = int(input())
    cycles.append(n)
cycles_height = [1]
is_spring = True
max_cycle = max(cycles)
for _ in range(max_cycle):
    last_height = cycles_height[len(cycles_height) - 1]
    if is_spring:
        cycles_height.append(last_height * 2)
    else:
        cycles_height.append(last_height + 1)
    is_spring = not is_spring
for i in cycles:
    print(cycles_height[i])
