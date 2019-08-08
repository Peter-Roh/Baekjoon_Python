import sys

N = int(sys.stdin.readline())
weight = [0] * N
height = [0] * N
ans = [0] * N
temp = 0

for i in range(N):
    weight[i], height[i] = map(int, sys.stdin.readline().split())

for i in range(N):
    for j in range(N):
        if weight[j] > weight[i] and height[j] > height[i]:
            temp += 1
    ans[i] = temp + 1
    temp = 0

print(*ans)
