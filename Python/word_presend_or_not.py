def is_here(a):
    b = "is"
    v  = a.split(" ")
    for i in range(len(v)):
        if b == v[i]:
            return "hai "
    return "Nahi hai "
a ="Word is not present in the sentence"
print(is_here(a))