for i in range(int(input())):
    l = input()
    cnt = 0
    ans = [ ]
    for j in range(len(l)):
        if l[j] == 'O':
            cnt += 1
            ans.append(cnt)
        else:
            cnt = 0
            ans.append(cnt)
    print(sum(ans))
