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

def day_in_year(year):
    return  366 if is_leap(year) else 365

def date_diff(first_day, second_day):
    first_list = [int(number) for number in first_day.split("-")]
    second_list = [int(number) for number in second_day.split("-")]
    sum = 0
    for i in range(first_list[2], second_list[2]):
        sum += day_in_year(i)
    print(sum)
    sum -= day_of_year(first_list[0], first_list[1], first_list[2])
    sum += day_of_year(second_list[0], second_list[1], second_list[2])
    return sum+1

print(date_diff("1-1-2018", "1-1-2020"))