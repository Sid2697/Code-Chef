import sys
t=int(input(''))
for i in range(t):
	n1,n2=sys.stdin.readline().split()
	n1=int(n1)
	n2=int(n2)
	if n1 < n2:
		print(n2,n1+n2)
	else:
		print(n1,n1+n2) 
