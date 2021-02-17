s = input()
count = 0
for i in range(len(s)):
    if i % 3 == 1:
        e = 'O'
    else:
        e = 'S'

    c = s[i]
    if c != e:
        count += 1
print(count)