scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
alice.reverse()
alice_reversed = alice
alice_reversed_index = 0
alice_rank = []
current_item_rank = 1
temp_value = scores[0]

# For alice scores that bigger than first value of score list
for value in alice_reversed:
    if value >= temp_value:
        alice_rank.append(1)
        alice_reversed_index += 1
    else:
        break

for value in scores:
    if alice_reversed_index == len(alice_reversed):
        break
    alice_score = alice_reversed[alice_reversed_index]
    if value < temp_value:
        current_item_rank += 1
    temp_value = value
    
    while alice_score >= value:
        alice_rank.append(current_item_rank)
        alice_reversed_index += 1
        if alice_reversed_index == len(alice_reversed):
            break
        alice_score = alice_reversed[alice_reversed_index]
        
# For alice scores that smaller than last value of score list
if alice_reversed_index < len(alice_reversed):
    while alice_reversed_index < len(alice_reversed):
        alice_rank.append(current_item_rank + 1)
        alice_reversed_index += 1
        
alice_rank.reverse()
for rank in alice_rank: print(rank)
