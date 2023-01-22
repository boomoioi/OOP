def is_plusone_dictionary(d):
    numberList = []
    for key, val in d.items():
        numberList.append(key)
        numberList.append(val)
    for i in range(1, len(numberList)):
        if numberList[i] - numberList[i-1] != 1:
            return False
    
    return True
             

print(is_plusone_dictionary({1:2, 3:10, 5:6, 7:8}))
