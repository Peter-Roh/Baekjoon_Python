import sys
ans = []

for i in range(int(sys.stdin.readline())):
    ans.append(int(sys.stdin.readline()))

ans.sort()

print('\n'.join(map(str, ans)))
