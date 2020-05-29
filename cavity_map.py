#!/bin/python3

n = int(input())
grid = []
for _ in range(n):
    grid_item = input()
    row = []
    for item in grid_item:
        row.append(item)
    grid.append(row)

row_count = len(grid)
column_count = len(grid[0])

indexes = []
for row_index, row in enumerate(grid):
    if row_index == 0 or row_index == row_count - 1:
        continue
    for column_index, column in enumerate(row):
        if column_index == 0 or column_index == column_count - 1:
            continue
        previous_column = row[column_index - 1]
        next_column = row[column_index + 1]
        previous_row = grid[row_index - 1][column_index]
        next_row = grid[row_index + 1][column_index]
        adjacent_cells = [previous_column, next_column, previous_row, next_row]
        not_cavity = False
        for cell in adjacent_cells:
            if cell >= column:
                not_cavity = True
                break
        if not not_cavity:
            indexes.append((row_index, column_index))

for index in indexes:
    grid[index[0]][index[1]] = "X"

for row in grid:
    row_str = ""
    for column in row:
        row_str += column
    print(row_str)
