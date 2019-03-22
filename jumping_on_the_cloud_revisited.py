nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
e = 100
current_index = 0
is_first_round = True
while(current_index != 0 or is_first_round):
    is_first_round = False
    new_index = (current_index + k) % n
    e -= 1
    value = c[new_index]
    if value == 1:
        e -= 2
    
    if new_index == 0:
        break
    if current_index + k >= n:
        current_index = 0
    else:
        current_index = new_index
print(e)
