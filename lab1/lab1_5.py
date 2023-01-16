def palindrome_checker(input_number):
    temp = input_number
    result_number = 0
    while(input_number>0):
        result_number *= 10
        result_number += input_number%10
        input_number = input_number // 10
    if(temp == result_number):
        return 1
    return 0 

max = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        temp = i*j
        if(temp <= max):
            break
        if(palindrome_checker(temp)):
            max = temp
print(max)
