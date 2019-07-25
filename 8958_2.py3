import sys

for i in range(int(sys.stdin.readline())):
    l = sys.stdin.readline()
    ans, cnt = 0, 0
    for j in l.split('X'):
        cnt = j.count('O')
        ans += int(cnt * (cnt + 1) / 2)
    print(ans)
