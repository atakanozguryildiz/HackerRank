import math
s = input()
s = s.replace(" ", "")
len_s = len(s)
sqrt_s = math.sqrt(len_s)
row_count = math.floor(sqrt_s)
col_count = math.ceil(sqrt_s)
while (row_count * col_count) < len_s:
    if row_count <= col_count:
        row_count += 1
    else:
        col_count += 1

matrix = []
for i in range(0, row_count):
    start_index = i * col_count
    end_index = start_index + col_count
    row = s[start_index:end_index]
    matrix.append(row)

result = ""
for i in range(0, col_count):
    col_text = ""
    for row in matrix:
        if i < len(row):
            result += row[i]
    result += col_text + " "
result = result.strip()
print(result)
