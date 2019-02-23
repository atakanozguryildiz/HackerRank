n = int(input())
p = list(map(int, input().rstrip().split()))
result = []
p.insert(0, -1)
for i in range(1, len(p)):
    # x = p(p(y))
    index = p.index(i)
    y = p.index(index)
    result.append(y)
for r in result:print(r)
