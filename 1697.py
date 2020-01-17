import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def walk(arr, visited):
    while visited[K] == 0:
        x = arr.popleft()
        if(0 <= x - 1 <= 100000 and visited[x - 1] == 0):
            arr.append(x - 1)
            visited[x - 1] = visited[x] + 1
        if(0 <= x + 1 <= 100000 and visited[x + 1] == 0):
            arr.append(x + 1)
            visited[x + 1] = visited[x] + 1
        if(0 <= 2 * x <= 100000 and visited[2 * x] == 0):
            arr.append(2 * x)
            visited[2 * x] = visited[x] + 1

arr = deque()
visited = [0] * 100001
arr.append(N)

if N >= K: 
    print(N - K)
else:
    walk(arr, visited)
    print(visited[K])
