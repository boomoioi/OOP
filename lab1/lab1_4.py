input_number = int(input())
number_list = []
for i in range(4):
    temp = 0 
    for j in range(i+1):
        temp = temp*10 + input_number 
        
    number_list.append(temp)

answer = 0

for i in range(4):
    answer += number_list[i]
    
print(answer)
