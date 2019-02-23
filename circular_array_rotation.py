nkq = input().split()
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(map(int, input().rstrip().split()))
queries = []
for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)
k = k % n
new_list_indexes = {}
for index, value in enumerate(a):
    new_index = (index + k) % n
    new_list_indexes[new_index] = value
for query in queries:
    v = new_list_indexes[query]
    print(v)
    
