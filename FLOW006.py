import sys
t=int(input(''))
for i in range(t):
	ans=0
	a=list()
	n1=sys.stdin.readline()
	for num in n1:
		a.append(num)
	del a[-1]
	for elem in a:
		elem = int(elem)
		ans += elem
	print(ans) 
