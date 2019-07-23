for i in range(int(input())):
    R, S = input().split()
    print(''.join([s * int(R) for s in S]))