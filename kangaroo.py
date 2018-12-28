x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
current_k1_point = x1 + v1
current_k2_point = x2 + v2
while True:
    if current_k1_point == current_k2_point:
        print("YES")
        break
    if v1 > v2 and current_k1_point > current_k2_point:
        print("NO")
        break
    elif v2 > v1 and current_k2_point > current_k1_point:
        print("NO")
        break
    elif v1 == v2:
        print("NO")
        break
    current_k1_point += v1
    current_k2_point += v2
