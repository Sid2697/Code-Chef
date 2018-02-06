import sys
t=int(input(''))
for i in range(t):
	n1,n2,n3=sys.stdin.readline().split()
	n1=int(n1)
	n2=int(n2)
	n3=int(n3)
	if (n1>n2 or n3>n2) and (n3<n2 or n1<n2):
		print(n2)
	elif (n2>n3 or n1>n3) and (n1<n3 or n2<n3):
		print(n3)
	elif (n3>n1 or n2>n1) and (n2<n1 or n3 < n1):
		print(n1) 
