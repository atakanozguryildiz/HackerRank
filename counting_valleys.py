n = int(input())
s = input()
current_level = 0
number_of_valley = 0
for i in range(len(s)):
    c = s[i]
    tmp_current = current_level
    if c is "U":
        current_level += 1
    elif c is "D":
        current_level -= 1

    if tmp_current == 0 and current_level == -1:
        number_of_valley += 1
print(number_of_valley)




