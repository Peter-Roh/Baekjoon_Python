import sys

year = int(sys.stdin.readline())

if (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0):
    ans = 1
else:
    ans = 0

print(ans)
