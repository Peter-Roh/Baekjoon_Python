S = input()
ans = ['-1'] * 26

for i in range(len(S)):
    if ans[ord(S[i]) - 97] == '-1':
        ans[ord(S[i]) - 97] = str(i)

print(' '.join(ans))
