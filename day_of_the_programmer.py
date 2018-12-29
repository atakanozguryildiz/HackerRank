year = int(input().strip())
february_day = 28
if year <= 1918 and year % 4 == 0:
    february_day = 29
else:
    if year % 400 == 0:
        february_day = 29
    elif year % 4 == 0 and year % 100 != 0:
        february_day = 29

days_of_year = [31, february_day, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]

if year == 1918:
    days_of_year[1] = february_day - 13

total_day = 0
for month in range(12):
    day_of_month = days_of_year[month]
    total_day += day_of_month
    if total_day > 256:
        difference = total_day - 256
        day = day_of_month - difference  - 1
        month = month + 1
        print("{:02d}.{:02d}.{}".format(day, month, year))
        break
