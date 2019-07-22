import sys

for i in range(int(input())):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #' + str(i + 1) + ': ' + str(A)  + ' + ' + str(B) + ' = ' + str(A + B))
