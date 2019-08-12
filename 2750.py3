N = int(input())
num = [0] * N

for i in range(N):
    num[i] = input()

num = list(map(str, sorted(num, key = int)))

for i in range(N):
    print(num[i])
