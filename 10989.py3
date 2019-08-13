import sys

ans = [0] * 10000

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ans[n - 1] += 1

for j in range(10000):
    if ans[j] == 0:
        pass
    else:
        print('%s\n' %(j + 1) * ans[j], end='')
