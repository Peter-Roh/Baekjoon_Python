import sys

print(''.join(sorted(list(sys.stdin.readline().rstrip()), key=int, reverse=True)))
