import operator
import sys

N = int(sys.stdin.readline())
num = [[0, 0] for i in range(N)]

for i in range(N):
    num[i][0], num[i][1] = map(int, sys.stdin.readline().split())

num.sort(key=operator.itemgetter(1, 0))

for i in range(N):
    print(num[i][0], num[i][1])
