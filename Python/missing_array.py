def find_missing(arr):
    maxi = max(arr)
    mini = min(arr)
    se = set(arr)
    missing = []
    for i in range(mini ,maxi+1):
        if i not in se:
            missing.append(i)
    return missing

arr = [6, 1, 4, 2, 8]
print(find_missing(arr))
