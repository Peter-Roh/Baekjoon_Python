def sum_num(a):
    return a + sum(list(map(int, str(a))))

import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    if sum_num(i) == N:
        print(i)
        break
    if i == N:
        print('0')
