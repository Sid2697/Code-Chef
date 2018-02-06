t=int(input(''))
for i in range(t):
	spaces = int(input())
	b=list(map(int, input().split()))
	minimum = min(b)
	b.remove(minimum)
	min1 = min(b)
	sum = minimum + min1
	print(sum) 
