n = int(input())
result = n
temp_n = n
while(True):
    n_ = temp_n - 1
    if n_ == 0:
        break
    result *= n_
    temp_n -= 1
print(result)
