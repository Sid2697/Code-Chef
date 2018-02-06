import sys
t=int(input(''))
for i in range(t):
	arr = list(map(int, input().split()))
	total = sum(arr)
	maximum = max(arr)
	if maximum == 180:
		print('NO')
	else:
		if total == 180:
			print('YES')
		else:
			print('NO')
	total = 0 
