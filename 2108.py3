import sys

def mean(N):
    sum_num = 0
    for j in range(8001):
        sum_num += cnt_num[j] * (j - 4000)
    return round(sum_num / N + 0.001)

def median(N):
    mid = N // 2
    for i in range(8001):
        if mid - cnt_num[i] >= 0:
            mid -= cnt_num[i]
        else:
            break
    return i - 4000

def max_cnt(N):
    sort_list = []
    max_cnt = max(cnt_num)
    for i in range(8001):
        if cnt_num[i] == max_cnt:
            sort_list.append(i - 4000)
    if len(sort_list) == 1:
        return sort_list[0]
    else:
        return sort_list[1]

def ran_val(N):
    j = 0; k = 8000
    while True:
        if cnt_num[j] == 0:
            j += 1
        else:
            break
    while True:
        if cnt_num[k] == 0:
            k -= 1
        else:
            break
    return k - j

cnt_num = [0] * 8001
N = int(sys.stdin.readline())

for i in range(N):
    temp = int(sys.stdin.readline())
    cnt_num[temp + 4000] += 1

print(mean(N))
print(median(N))
print(max_cnt(N))
print(ran_val(N))
