a = [1,2,33,57,21,11,44]
ma1 = a[0]
ma2 = a[0]
for i in a:
    if ma1 < i:
        ma1 = i
for i in a:
    if ma1 > i and i > ma2:
        ma2 = i
print(f"First Maximum: {ma1}, Second Maximum: {ma2}")