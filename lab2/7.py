day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    ans = 0
    if year % 400 == 0:
        ans = 1
    elif year%100 != 0 and year%4 == 0:
        ans = 1
    return ans 


def day_of_year(day, month ,year):
    sum = 0 
    if is_leap(year):
        day_in_month[2] = 29
    for i in range(month):
        sum += day_in_month[i]
    sum += day
    return sum
