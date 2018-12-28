s = input()
is_am = "AM" in s 
first_two_digits = s[:2]
if is_am:
    if first_two_digits == "12":
        print(("00" + s[2:-2]))
    else:
        print(s[:-2])
else:
    if first_two_digits == "12":
        print(s[:-2])
    else:
        pm_hour = str(int(first_two_digits) + 12)
        print((pm_hour + s[2:-2]))

