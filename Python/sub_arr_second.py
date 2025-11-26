
def isSubset( a, b):
    
    for j in range(len(b)):
        if b[j]  in a:
            a.remove(b[j])
        else:
            return("No")
        
    return("Yes")
    

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
print(isSubset(a,b))