N = int(input())

for i in range(1, N):
    print(' ' * (N - i - 1), '*' * i)
print('*' * N)
