N = int(input())
cnt = 0

if N < 10:
    N = N * 10

a = N

while True:
    a = 10 * (a % 10) + ((a // 10) + (a % 10)) % 10
    cnt  += 1
    if N == a:
        break

print(cnt)
