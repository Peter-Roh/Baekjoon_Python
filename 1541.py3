import sys

exp = sys.stdin.readline()
arr = []
arr = exp.split('-')
ans = 0; l = len(arr)

if l == 1:
        arr = exp.split('+')
        for i in range(len(arr)):
            ans += int(arr[i])
        print(ans)
else: 
    for i in range(l):
        if '+' in arr[i] and i != 0:
            temp = arr[i].split('+')
            for j in range(len(temp)):
                ans -= int(temp[j])
        elif '+' not in arr[i] and i == 0:
            ans += int(arr[i])
        elif '+' in arr[i] and i == 0:
            temp = arr[i].split('+')
            for j in range(len(temp)):
                ans += int(temp[j])
        else:
            ans -= int(arr[i])
    print(ans)
