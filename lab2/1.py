number_list = input().split()
number_list = list(map(int, number_list))
number_list.sort()

checker = 0 
sum = 0
multiplier = 1

for i in range(len(number_list)):
    if(checker == 1):
        sum = sum*10 + number_list[i]
    else:
        if(number_list[i] != 0):
            sum = number_list[i] * multiplier
            checker = 1
        else:
            multiplier *= 10
    
print(sum)
        