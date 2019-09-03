import sys

def gcd(x, y):
    while x != 0 and y != 0:
        if x > y:
            if x % y == 0:
                return y
            x = x % y
        else:
            if y % x == 0:
                return x
            y = y % x

def lcm(x, y):
    g = gcd(x, y)
    div_x = x // g
    div_y = y // g
    return div_x * div_y * g

a, b = map(int, sys.stdin.readline().split())
print("{}\n{}" .format(gcd(a, b), lcm(a, b)))
