import sys

PI = 3.14159265358979

r = int(sys.stdin.readline())

print("{:0.6f}\n{:0.6f}".format(PI * r * r, 2 * r * r))