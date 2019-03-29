t = int(input())
for t_itr in range(t):
    bw = input().split()
    b = int(bw[0])
    w = int(bw[1])
    bcWcz = input().split()
    bc = int(bcWcz[0])
    wc = int(bcWcz[1])
    z = int(bcWcz[2])
    min_price = min(bc, wc)
    max_price = max(bc, wc)
    new_price = min_price + z
    if bc == wc or new_price >= max_price:
        # calculate normally
        price = b * bc + w * wc
        print(price)
        continue
    max_gift = b if max_price == bc else w
    min_gift = b if min_price == bc else w
    price = new_price * max_gift + min_gift * min_price
    print(price)
    continue
