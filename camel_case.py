s = input()

upper_count = sum(map(str.isupper, s))
word_count = upper_count + 1
print(word_count)