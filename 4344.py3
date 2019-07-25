import sys

cnt = 0

for i in range(int(sys.stdin.readline())):
    arr = list(map(int, sys.stdin.readline().split()))
    mean = (sum(arr) - arr[0]) / arr[0]
    for j in arr[1:]:
        if j > mean:
            cnt += 1
    print('%.3f' %(cnt * 100 / arr[0]) + '%')
    cnt = 0
