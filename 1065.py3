def is_han(n):
    if int(n) <= 99:
        return 1
    if (int(n[0]) - int(n[1])) == (int(n[1]) - int(n[2])):
        return 1
    else:
        return 0

N = input()
cnt = 0

for i in range(1, int(N) + 1):
    if is_han(str(i)) == 1:
        cnt += 1

print(cnt)
