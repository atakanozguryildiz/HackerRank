def totals(matrix):
    first_column = 0
    second_column = 0
    third_column = 0
    diagonal = 0
    diagonal2 = 0
    rows = []
    diagonal2_index = len(matrix[0]) - 1
    for i in range(len(matrix)):
        row = matrix[i]
        first_column += row[0]
        second_column += row[1]
        third_column += row[2]
        diagonal += row[i]
        diagonal2 += row[diagonal2_index]
        diagonal2_index -= 1
        rows.append(sum(row))

    first_row, second_row, third_row = rows[0], rows[1], rows[2]
    return first_row, second_row, third_row, first_column, second_column, third_column, diagonal, diagonal2


def find_differences(s1, s2):
    difference = 0
    row_count = len(s1)
    column_count = len(s1[0])
    for i in range(row_count):
        for j in range(column_count):
            element1 = s1[i][j]
            element2 = s2[i][j]
            difference += abs(element1 - element2)
    return difference


def is_magic(s):
    results = totals(s)
    first = results[0]
    for i in results[1:]:
        if first != i:
            break
    else:
        return True
    return False


def convert_tuple_to_matrix(t):
    result = []
    temp = []
    for i in t:
        temp.append(i)
        if len(temp) == 3:
            result.append(temp)
            temp = []
    return result

s = []
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

import itertools
from functools import partial
all_posibilities = list(map(convert_tuple_to_matrix, list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]))))
mapfunc = partial(find_differences, s2=s)
magics = list(filter(is_magic, all_posibilities))
differences = list(map(mapfunc, magics))
print(min(differences))

