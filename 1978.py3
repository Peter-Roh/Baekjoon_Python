import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    if i == 1:
        N -= 1
    elif i % 2 == 0 and i != 2:
        N -= 1
    elif i % 3 == 0 and i != 3:
        N -= 1
    elif i % 5 == 0 and i != 5:
        N -= 1
    elif i % 7 == 0 and i != 7:
        N -= 1
    elif i % 9 == 0 and i != 9:
        N -= 1
    elif i % 11 == 0 and i != 11:
        N -= 1
    elif i % 13 == 0 and i != 13:
        N -= 1
    elif i % 17 == 0 and i != 17:
        N -= 1
    elif i % 19 == 0 and i != 19:
        N -= 1
    elif i % 23 == 0 and i != 23:
        N -= 1
    elif i % 29 == 0 and i != 29:
        N -= 1
    elif i % 31 == 0 and i != 31:
        N -= 1


print(N)
