n = int(input())
password = input()

special_characters = "!@#$%^&*()-+"

is_in_special_chars = lambda x: x in special_characters

is_low_ok = False
is_upp_ok = False
is_num_ok = False
is_spec_ok = False
for c in password:
    if is_low_ok and is_upp_ok and is_num_ok and is_spec_ok:
        break
    if str.islower(c):
        is_low_ok = True
    elif str.isupper(c):
        is_upp_ok = True
    elif str.isnumeric(c):
        is_num_ok = True
    elif is_in_special_chars(c):
        is_spec_ok = True


required_fields = len(list(filter(lambda x: x is False, [is_low_ok, is_upp_ok, is_num_ok, is_spec_ok])))

if n + required_fields >= 6:
    count = required_fields
else:
    count = 6 - (n + required_fields) + required_fields
print(count)