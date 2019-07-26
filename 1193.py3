X = int(input())
i = 1
while i* (i + 1) / 2 < X:
    i += 1
i -= 1

if i % 2 == 1:
    print('{}/{}' .format(X - int(i * (i + 1) / 2), i + 2 - X + int(i * (i + 1) / 2)))
else:
    print('{}/{}' .format( i + 2 - X + int(i * (i + 1) / 2), X - int(i * (i + 1) / 2)))
