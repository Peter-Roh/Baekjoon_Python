import sys

T = int(sys.stdin.readline())
l = list(map(int, sys.stdin.read().split()))

for i in range(0, 2 * T, 2):
    print(l[i] + l[i + 1])
