q = int(input())
strings = []
for q_itr in range(q):
    s = input()
    h = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    pos = 0
    final_pos = 10
    is_success = False
    for i in s:
        c = h[pos]
        if i == c:
            pos += 1
        if pos == final_pos:
            is_success = True
            break
    if is_success:
        print("YES")
    else:
        print("NO")