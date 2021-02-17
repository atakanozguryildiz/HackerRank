l = int(input().strip())
s = input()
chars = dict()
deleted_chars = set()
for i in range(len(s)):
    c = s[i]
    if c not in chars:
        chars[c] = [i]
        continue
    indexes = chars[c]
    indexes.append(i)
    chars[c] = indexes
    indexes_len = len(indexes)
    if indexes[indexes_len - 1] == indexes[indexes_len - 2] + 1:
        deleted_chars.add(c)

for dc in deleted_chars:
    chars.pop(dc)

most_chars_sorted = sorted(chars, key=lambda x:len(chars[x]), reverse=True)

result = 0
for i in range(len(most_chars_sorted)):
    for j in range(i+1, len(most_chars_sorted)):
        most_char = most_chars_sorted[i]
        most_second_char = most_chars_sorted[j]
        most_char_items = chars[most_char]
        most_second_char_items = chars[most_second_char]
        final_index_list = sorted(most_char_items + most_second_char_items)
        turn = None
        broken = False
        for index in final_index_list:
            if turn is None:
                if index in most_char_items:
                    turn = most_char
                else:
                    turn = most_second_char
                continue
            who_next = most_char if index in most_char_items else most_second_char
            if who_next != turn:
                turn = who_next
            else:
                broken = True
                break

        if broken:
            continue

        if len(final_index_list) > result:
            result = len(final_index_list)
print(result)