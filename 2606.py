import sys

N = int(sys.stdin.readline())
T = int(sys.stdin.readline())
flag = N

arr = [0] * N

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    if arr[a - 1] == 0 and arr[b - 1] == 0:
        arr[a - 1] = flag
        arr[b - 1] = flag
        flag -= 1
    elif arr[a - 1] != 0 and arr[b - 1] == 0:
        arr[b - 1] = arr[a - 1]
    elif arr[a - 1] == 0 and arr[b - 1] != 0:
        arr[a - 1] = arr[b - 1]
    elif arr[a - 1] != 0 and arr[b - 1] != 0:
        if arr[a - 1] != arr[b - 1]:
            temp = arr[a - 1]
            for j in range(N):
                if arr[j] == temp:
                    arr[j] = arr[b - 1]

print(arr.count(arr[0]) - 1)
