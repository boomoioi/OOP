def is_plusone_dictionary(d):
    numberList = []
    for key, val in d.items():
        numberList.append(key)
        numberList.append(val)
    for i in range(1, len(numberList)):
        if numberList[i] - numberList[i-1] != 1:
            return False
    
    return True
             

