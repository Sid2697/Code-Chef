import sys
t=int(input(''))
for i in range(t):
	num=sys.stdin.readline()
	length=len(num)
	first=num[0]
	last=num[length-2]
	sum=int(first)+int(last)
	print(sum) 
