import sys
t=int(input(''))
for i in range(t):
	n=0
	y=0
	ind=0
	n=int(sys.stdin.readline())
	a=sys.stdin.readline()
	for letters in a:
		if letters == 'N':
			n+=1
		elif letters == 'Y':
			y+=1
		elif letters == 'I':
			ind+=1 
	if ind >= 1:
		print('INDIAN')
	elif y >= 1:
		print('NOT INDIAN')
	else:
		print('NOT SURE')		
