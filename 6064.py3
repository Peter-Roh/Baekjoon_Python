import sys

def solve(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1

for i in range(int(sys.stdin.readline())):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(solve(M, N, x, y))
