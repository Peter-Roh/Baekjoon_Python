num = input()
ans = len(num)

for x in num:
    if x == 'A' or x == 'B' or x == 'C':
        ans += 2
    elif x == 'D' or x == 'E' or x == 'F':
        ans += 3
    elif x == 'G' or x == 'H' or x == 'I':
        ans += 4
    elif x == 'J' or x == 'K' or x == 'L':
        ans += 5
    elif x == 'M' or x == 'N' or x == 'O':
        ans += 6
    elif x == 'P' or x == 'Q' or x == 'R' or x == 'S':
        ans += 7
    elif x == 'T' or x == 'U' or x == 'V':
        ans += 8
    else:
        ans += 9

print(ans)
