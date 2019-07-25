sum = 0
N = int(input())
score = list(map(int, input().split()))
M = max(score)
for i in score:
    sum += i / M * 100
print(sum / N)
