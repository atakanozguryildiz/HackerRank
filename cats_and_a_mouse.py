q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    x_difference = abs(z - x)
    y_difference = abs(z - y)
    if x_difference == y_difference:
        print("Mouse C")
    elif x_difference > y_difference:
        print("Cat B")
    else:
        print("Cat A")
