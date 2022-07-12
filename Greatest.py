def large(a,b,c):
    if a>b and a>c:
        large=a
    elif b>a and b>c:
        large=b
    elif c>a and c>b:
        large=c
    return large

print(large(12,96957,14))


