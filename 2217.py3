import sys

N = int(sys.stdin.readline())
rope = []; ans = 0

for i in range(N):
    rope.append(int(sys.stdin.readline()))
rope.sort()

for i in range(N):
    ans = max(ans, rope[i] * (N - i))

print(ans)
