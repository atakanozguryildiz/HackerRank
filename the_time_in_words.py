#!/bin/python3

numbers_map = {
   0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

def number_to_word(n):
    if n < 20:
        return numbers_map[n]
    elif n in range(20, 30):
        first_rep = 'twenty'
    elif n in range(30, 40):
        first_rep = 'thirty'
    elif n in range(40, 50):
        first_rep = 'forty'
    elif n in range(50, 60):
        first_rep = 'fifty'
    second_rep = numbers_map[int(list(str(n))[1])]
    if second_rep == 'zero':
        return first_rep
    else:
        result = "{} {}".format(first_rep, second_rep)
        return result


h = int(input())
m = int(input())

h_word = number_to_word(h)
if m == 0:
    print("{} o' clock".format(h_word))
elif m == 30:
    print("half past {}".format(h_word))
elif m == 45:
    h_word = number_to_word(h+1)
    print("quarter to {}".format(h_word))
elif m == 15:
    print("quarter past {}".format(h_word))
elif m > 30:
    m_word = number_to_word(60-m)
    h_word = number_to_word(h+1)
    if m_word == 'one':
        time = 'minute'
    else:
        time = 'minutes'
    print("{} {} to {}".format(m_word, time, h_word))
elif m < 30:
    m_word = number_to_word(m)
    if m_word == 'one':
        time = 'minute'
    else:
        time = 'minutes'
    print("{} {} past {}".format(m_word, time, h_word))
