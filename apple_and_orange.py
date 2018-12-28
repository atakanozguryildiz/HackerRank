st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

apple_locations = [(a + apple) for apple in apples]
orange_locations = [(b + orange) for orange in oranges]
house_range = range(s, t+1)
apples = len(list(filter(lambda x:x in house_range, apple_locations)))
oranges = len(list(filter(lambda x:x in house_range, orange_locations)))
print(apples)
print(oranges)

