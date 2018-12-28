n = int(input())
for i in range(n):
	empty_space_count = (n - 1) - i
	square_count = n - empty_space_count
	result = empty_space_count * " " + square_count * "#"
	print(result)

