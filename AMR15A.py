t=int(input(''))
while True:
	e,o=0,0
	arr = list(map(int, input().split()))
	for num in arr:
		if num%2 == 0:
			e+=1
		else:
			o+=1
	if e>o:
		print('READY FOR BATTLE')
	else:
		print('NOT READY')
	break 
