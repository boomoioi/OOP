def add2list(lst1,lst2):
    return [lst1[i]+lst2[i] for i in range(len(lst2))]

x = [1,2,3]
y = [3,2,1]
print(add2list(x,y))