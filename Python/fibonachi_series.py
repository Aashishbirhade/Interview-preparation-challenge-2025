def fibonachi_series(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    
    arr = [0,1]
    for i in range(2,n):
        arr.append(arr[-1]+ arr[-2])
    return arr
n = 10
print(fibonachi_series(n))