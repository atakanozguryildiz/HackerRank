n = int(input())
ar = list(map(int, input().rstrip().split()))
total_sock_counts = dict()
for sock in ar:
    total_sock_counts[sock] = total_sock_counts.get(sock, 0) + 1

sock_counts = total_sock_counts.values()
print(sum(map(lambda x:int(x/2), sock_counts)))
