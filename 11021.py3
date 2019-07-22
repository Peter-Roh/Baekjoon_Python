import sys

for i in range(int(input())):
    X = sum(map(int, sys.stdin.readline().split()))
    print('Case #{0}: {1}'.format(int(i) + 1, X))
