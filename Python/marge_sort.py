def marge_sort(a,b):
    i = 0
    j = 0
    li = []
    while i < len(a) and j <len(b):
        if a[i] < b[j]:
            li.append(a[i])
            i += 1
        else:
            li.append(b[j])
            j += 1
    while i < len(a):
        li.append(a[i])
        i += 1
    while j < len(b):
        li.append(a[j])
        j += 1
    
    return li
        


a = [1,12,43,47,54,76]
b = [2,24,53,89]
print(marge_sort(a,b))