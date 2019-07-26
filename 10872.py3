def fac(n):
    s = 1
    for i in range(1, n +1):
        s *= i
    return s

print(fac(int(input())))
