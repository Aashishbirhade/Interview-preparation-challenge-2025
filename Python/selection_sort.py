a = [10,3,44,65,22,67,6,41]
for i in range(len(a)):
    min = i
    for j in range(i,len(a)):
        if a[min] > a[j]:
            min = j
    a[min],a[i] = a[i],a[min]
print(a)