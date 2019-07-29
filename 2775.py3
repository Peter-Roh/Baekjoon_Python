import sys

matrix = [[0] * 15 for i in range(15)]
matrix[1][1] = 1

for j in range(15):
    matrix[0][j] = j

for i in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            matrix[i][j] = matrix[i -1][j] + matrix[i][j - 1]
    print(matrix[k][n])
