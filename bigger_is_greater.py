#!/bin/python3
T = int(input())
inputs = []
outputs = []
for T_itr in range(T):
    w = input()
    inputs.append(w)
for s in inputs:
    s_length = len(s)
    check_range = 2
    is_exist = False
    min_distance = None
    while(check_range<=len(s)):
        uncheck_part = s[:-check_range]
        check_part = s[-check_range:]
        alt_subs = []
        len_sub_s = len(check_part)
        for i in range(len_sub_s-1, -1, -1):
            if i == 0:
                break
            c = check_part[i]
            first_index = None
            distance_for_swap = None
            for j in range(i-1, -1, -1):
                c_c = check_part[j]
                if c > c_c:
                    first_index = j
                    distance_for_swap = i - j
                    if min_distance is None:
                        min_distance = distance_for_swap
                    break
            if first_index is not None:
                check_part = list(check_part)
                temp_c = check_part[first_index]
                check_part[first_index] = c
                check_part[i] = temp_c
                check_part = "".join(check_part)
                first_part = check_part[:first_index+1]
                second_part = check_part[first_index+1:]
                second_part = list(sorted(second_part))
                final = "".join(first_part) + "".join(second_part)
                alt_subs.append(final)
                if distance_for_swap == 1 or distance_for_swap < min_distance:
                    break # Its not possible to find smaller
                min_distance = distance_for_swap
        if len(alt_subs) > 0:
            first_sub = list(sorted(alt_subs))[0]
            result = uncheck_part + "".join(first_sub)
            print(result)
            is_exist = True
            break
        check_range += 1
    if not is_exist:
        print("no answer")



