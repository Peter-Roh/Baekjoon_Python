def sum_num(n):
    return sum(map(int, str(n)))

def d_func(n):
    return n + sum_num(n)

set_A = set([x for x in range(1, 10001)])
set_B = set([d_func(x) for x in range(1, 10001)])

for i in sorted(set_A - set_B):
    print(i)
