#!/bin/python3

nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
page = 1
pages_and_indexes = {}
special_problem = 0
for chapter_index in range(n):
    problem_start_index = 1
    problem_count = arr[chapter_index]
    while problem_count > 0:
        if problem_count >= k:
            r = range(problem_start_index, problem_start_index+k)
        else:
            r = range(problem_start_index, problem_start_index+problem_count)

        problem_count -= k
        pages_and_indexes[page] = r
        problem_start_index += k
        page += 1
for p in pages_and_indexes:
    rr = pages_and_indexes[p]
    if p in rr:
        special_problem += 1
print(special_problem)