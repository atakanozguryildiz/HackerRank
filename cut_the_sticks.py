n = int(input())
arr = list(map(int, input().rstrip().split()))
lengths = [len(arr)]
while(True):
    min_elem = min(arr)
    arr = list(filter(lambda x:x>0,list(map(lambda x: x -min_elem, arr))))
    len_of_new_arr = len(arr)
    if len_of_new_arr == 0:
        break
    lengths.append(len_of_new_arr)
for i in lengths:print(i)
