#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    square_matrix = get_square_matrix(find_each_row_length_in_matrix(arr))
    
    first_diagonal_total = 0
    second_diagonal_total = 0
    first_current_index = 0
    second_current_index = len(square_matrix[0]) - 1
    for row in square_matrix:
        first_diagonal_item = row[first_current_index]
        second_diagonal_item = row[second_current_index]
        first_diagonal_total += first_diagonal_item
        second_diagonal_total += second_diagonal_item
        first_current_index += 1
        second_current_index -= 1

    return abs((first_diagonal_total - second_diagonal_total))


def get_square_matrix(row_and_length):

    rows = []
    lengths = []
    for row, length in row_and_length:
        rows.append(row)
        lengths.append(length)
    total_element_count = len(row_and_length)
    for i in range(total_element_count):
        row_length = lengths[i]
        if row_length <= 1:
            continue
        if (i + row_length) > total_element_count:
            continue
        
        check_arr_lengths = lengths[i:i+row_length]
        check_arr_rows = rows[i:i+row_length]
        is_fail = False
        result_arr = []
        for j in range(len(check_arr_lengths)):
            check_row_length = check_arr_lengths[j]
            if check_row_length < row_length:
                is_fail = True
                break
            else:
                check_row = check_arr_rows[j][:row_length]
                result_arr.append(check_row)
        if is_fail:
            continue
        
        return result_arr
    return None
        

def find_each_row_length_in_matrix(arr):
    arr_length = len(arr)
    row_and_length = []
    for i in range(arr_length):
        row = arr[i]
        row_and_length.append((row,len(row)))
    return row_and_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

