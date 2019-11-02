#!/bin/python3
p = int(input())
q = int(input())

numbers = []

for number in range(p, q+1, 1):
    square = number ** 2
    square_str = str(square)
    number_len = len(str(number))
    square_len = len(square_str)
    if square_len == 1:
        if square == number:
            numbers.append(str(number))
        continue
    right_part = square_str[-number_len:]
    left_part = square_str[:(square_len-number_len)]
    first_num = int(left_part)
    second_num = int(right_part)
    if first_num + second_num == number:
        numbers.append(str(number))
if not numbers:
    print("INVALID RANGE")
else:
    print(" ".join(numbers))
