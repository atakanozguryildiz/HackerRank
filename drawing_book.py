n = int(input())
p = int(input())

p = p if p % 2 == 0 else p - 1
n = n if n % 2 == 0 else n - 1
front_page_count = int((p - 0) / 2)
back_page_count = int((n - p) / 2)
print(min([front_page_count, back_page_count]))
