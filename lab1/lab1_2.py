count_upper = 0
count_lower = 0
input_string = input()
for i in input_string:
    if(i.isupper()):
        count_upper+=1
    elif(i.islower()):
        count_lower+=1
print(f"{count_upper}\n{count_lower}")