bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = sorted(list(map(int, input().rstrip().split())),reverse=True)
drives = list(map(int, input().rstrip().split()))
all_valid_prices = []
for i in range(len(keyboards)):
    key_price = keyboards[i]
    prices = list(filter(lambda x : x<= b,list(map(lambda x:x+key_price, drives))))
    all_valid_prices.extend(prices)

if all_valid_prices:
    print(max(all_valid_prices))
else:
    print(-1)
