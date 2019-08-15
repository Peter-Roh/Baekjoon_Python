import sys

N, K = map(int, sys.stdin.readline().split())
A = []; t = 1; cnt = 0

for i in range(N):
    A.append(int(sys.stdin.readline()))

A.reverse()

for i in A:
    if i <= K:
        t = K // i
        K = K % i
        cnt += t

print(cnt)
