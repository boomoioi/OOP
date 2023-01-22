def delete_minus(x):
    return [[second for second in first if second >= 0] for first in x]
    
print(delete_minus([ [1, -3, 2], [-8, 5], [-1, -4, -3] ]))