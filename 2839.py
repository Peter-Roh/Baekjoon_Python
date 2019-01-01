N = int(input())
x = 0

while(N >= 0):
	if(N % 5 == 0):
		sum = x + N / 5
		break
	else:
		N = N - 3

	x += 1

if(N < 0):
	sum = -1

print(int(sum))