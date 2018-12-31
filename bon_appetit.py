nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
bill.pop(k)
anna_actual = int(sum(bill) / 2)
    print("Bon Appetit")
else:
    print(b - anna_actual)

