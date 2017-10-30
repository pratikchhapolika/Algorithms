def myPow(x, n):
    if n == 0:
        return 1
    
    if n<0:
        n = -n
        x = 1/x

    total = 1
    while n>0:
        if n%2!=0:
            total*=x
        x = x*x
        n = n//2

    return total

print myPow(4, 6)
print myPow(2, 4)


