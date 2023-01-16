def count_minus(str):
    return len([int(x) for x in str.split() if int(x) < 0])

str = input()
print(count_minus(str))