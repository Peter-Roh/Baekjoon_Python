import sys

N = int(sys.stdin.readline())
arr = [[0, 0]] * N

for i in range(N):
    arr[i] = sys.stdin.readline().split()
    arr[i][0] = int(arr[i][0])

arr.sort(key = lambda element: element[0])

for i in range(N):
    print(arr[i][0], arr[i][1])
