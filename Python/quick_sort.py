def partition(a, low, high):
    pivot = a[low]
    i = low + 1
    j = high

    while i <= j:
        while i < high and a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]  # swap
            i += 1
            j -= 1
        else:
            i += 1

    a[low], a[j] = a[j], a[low]
    return j


def Quick(a, low, high):
    if low >= high:
        return
    pvtloc = partition(a, low, high)
    Quick(a, low, pvtloc - 1)
    Quick(a, pvtloc + 1, high)


a = [20, 5, 15, 10, 35, 30]

print("Original array:", a)

Quick(a, 0, len(a) - 1)

print("Sorted array:", a)
