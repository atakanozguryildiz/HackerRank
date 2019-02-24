s = input()
t = input()
k = int(input())

# 1. Delete all and add again scenario
delete_item_count = len(s)
addition_item_count = len(t)
if delete_item_count + addition_item_count < k:
    print("Yes")
elif s is t and k % 2 == 0:
    # 2. If they are same, only add delete and add last char for complete k action
    print("Yes")
else:
# 3. Delete only needed chars and add again
    exact_match = 0
    if len(t) > len(s):
        max_list = t
        min_list = s
    else:
        max_list = s
        min_list = t
    for i, c in enumerate(min_list):
        c_ = max_list[i]
        if c is c_:
            exact_match += 1
        else:
            break
    temp_k = 0
    delete_item_count = len(s[exact_match:])
    addition_item_count = len(t) - len(s[:exact_match])
    temp_k = delete_item_count + addition_item_count
    if temp_k > k:
        print("No")
    elif temp_k == k:
        print("Yes")
    elif (k-temp_k) % 2 == 0:
        print("Yes")
    else:
        print("No")


