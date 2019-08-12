N = int(input())
doom = '666'
i = 665
while N > 0:
    while i > 0:
        i += 1
        if doom in str(i):
            N -= 1
            break

print(i)
