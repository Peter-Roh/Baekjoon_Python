S = input().upper()
ans = [0] * 26
for i in range(len(S)):
    ans[ord(S[i]) - 65] = (ans[ord(S[i]) - 65]) + 1

if ans.count(max(ans)) >= 2:
    print('?')
else:
    print(chr(ans.index(max(ans)) + 65))
