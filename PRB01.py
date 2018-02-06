t=int(input(''))
for i in range(t):
	count = 0
	n=100000
	num = int(input(''))
	while n >= 1:
		if num%n == 0:
			count += 1
		n-=1
	if count > 2 :
		print('no')
	else:
		print('yes')
