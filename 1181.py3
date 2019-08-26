import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(sys.stdin.readline())

arr = list(set(arr))

arr.sort(key= lambda arr: (len(arr), arr))

for i in range(len(arr)):
    print(arr[i], end='')
