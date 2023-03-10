day_in_month = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    ans = 0
    if year % 400 == 0:
        ans = 1
    elif year%100 != 0 and year%4 == 0:
        ans = 1
    return ans 


def day_of_year(day, month ,year):
    day_in_month = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
    sum = 0 
    
    if is_leap(year):
        day_in_month[2] = 29

    for i in range(month):
        sum += day_in_month[i]

    sum += day
    return sum

def day_in_year(year):
    return  366 if is_leap(year) else 365

def date_diff(date1, date2):
    first_list = [int(number) for number in date1.split("-")]
    second_list = [int(number) for number in date2.split("-")]
    day_list = [first_list, second_list]

    

    for i in range(2):
        day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]    
        month_index = day_list[i][1]
        day = day_list[i][0]
        if(is_leap(day_list[i][2])):
            day_in_month[1] = 29
        if(month_index > 12 or month_index < 1):
            return -1
        if(day > day_in_month[month_index] or day < 1):
            return -1

    sum = 0

    for i in range(first_list[2], second_list[2]):
        sum += day_in_year(i)

    sum -= day_of_year(first_list[0], first_list[1], first_list[2])
    sum += day_of_year(second_list[0], second_list[1], second_list[2])

    return sum+1

print(date_diff("1-1-2019", "1-1-2020"))