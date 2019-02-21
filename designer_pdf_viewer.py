h = list(map(int, input().rstrip().split()))
word = input()

alphabet = {"a":0, "b":1, "c":2, "d":3, "e":4,
            "f":5, "g":6, "h":7, "i":8, "j":9,
            "k":10, "l":11, "m":12, "n":13, "o":14,
            "p":15, "q":16, "r":17, "s":18, "t":19, "u":20,
            "v":21,"w":22, "x":23, "y":24, "z":25}
max_length = 0
for c in word:
    if h[alphabet[c]] > max_length:
        max_length = h[alphabet[c]]
print(len(word) * max_length)
