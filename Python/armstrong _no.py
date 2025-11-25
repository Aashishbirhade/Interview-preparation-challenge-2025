def isarmstrong_no(a):
    n = len(str(a))
    b = a
    sumi = 0
    while a!=0:
        rem = a%10
        sumi += rem **n
        a //= 10
    return sumi == b

a =153
if isarmstrong_no(a):
    print("yes")
else:
    print("No")