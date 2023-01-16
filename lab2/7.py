def is_leap(year):
    ans = 0
    if year % 400 == 0:
        ans = 1
    elif year%100 != 0 and year%4 == 0:
        ans = 1
    return ans 


def day_of_year(day, month ,year):
    month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
    sum = 0 
    if is_leap(year):
        month_day[1] = 29
    for i in range(month-1):
        sum += month_day[i]
    sum += day
    return sum

print(day_of_year(1,1,2020))