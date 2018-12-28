n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
total = d; count = m
number_of_cakes = 0
for i in range(len(s)):
    if (i + count) <= len(s):
        segment = s[i:(i+count)]
        segment_total = sum(segment)
        if segment_total == total:
            number_of_cakes += 1
print(number_of_cakes)
        



