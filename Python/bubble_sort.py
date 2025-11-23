def is_bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
a = [21,4,33,56,34,655,54,77,45,3]
print(is_bubble(a))