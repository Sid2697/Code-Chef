import sys
t=int(input(''))
for i in range(t):
	num = int(sys.stdin.readline())
	if num < 10:
		print('What an obedient servant you are!')
	else:
		print('-1') 
