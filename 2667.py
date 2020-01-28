import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(data, i, j, N, cnt):
    data[i][j] = 0
    queue = []
    queue.append((i, j))
    while len(queue) > 0:
        i, j = queue.pop()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x and x < N and 0 <= y and y < N:
                if data[x][y] == 1:
                    cnt += 1
                    data[x][y] = 0
                    queue.append((x, y))
    return cnt

N = int(sys.stdin.readline())
data = [list(map(int, list(sys.stdin.readline().strip()))) for i in range(N)]
ans = []
cnt = 1

for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            ans.append(check(data, i, j, N, cnt))

print(len(ans))
for i in sorted(ans):
    print(i)
