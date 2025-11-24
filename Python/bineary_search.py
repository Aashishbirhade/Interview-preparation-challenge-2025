def bineary_search(a):
    st = 0
    end = len(a)-1
    k = 56
    while st <= end:
        mid = st + end //2
        if a[mid] == k:
            return mid
        elif a[mid] > k:
            end = mid- 1
        elif a[mid] < k:
            st = mid +1
    return "Not found"
a = [232,43,56,777,33,67]
print(bineary_search(a))
