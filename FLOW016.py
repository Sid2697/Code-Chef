def gcd(a,b):
	r=a%b
	if r==0:
		return b
	else:
		c = gcd(b,r)
		return c
t = int(input(''))
for i in range(t):
	n1,n2=input('').split()
	n1=int(n1)
	n2=int(n2)
	gcd1 = gcd(n1,n2)
	lcm = (n1*n2)/gcd1
	print(gcd1,int(lcm)) 
