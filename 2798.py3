import sys

N, M = map(int, sys.stdin.readline().split())
num = [0] * N
ans = 0

num = list(sorted(map(int, sys.stdin.readline().split())))

for i in range(N):
    if num[i] >= M - 1:
        del num[i:]
        break

N = len(num)

if N == 3:
    for i in range(N):
        ans += num[i]
else:
    for i in range(N - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            for k in reversed(range(N)):
                if k == i or k == j:
                    continue
                if num[k] <= M - num[i] - num[j]:
                    temp = num[k] + num[i] + num[j]
                    if ans == 0 or ans < temp:
                        ans = temp
                    break
            if ans == M:
                break
        if ans == M:
            break

print(ans)
