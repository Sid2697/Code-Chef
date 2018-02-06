import sys
t=int(input(''))
for i in range(t):
	a=list()
	n1=sys.stdin.readline()
	for num in n1:
		a.append(num)
	a.reverse()
	del a[0]
	b=0
	for num in a:
		if num=='0':
			b+=1
		else:
			break
	for d in range(b):
		del a[0]
	print(*a,sep='')     #Way to print a list side by side
	 
