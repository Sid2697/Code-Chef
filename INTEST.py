import sys
t1,t2=sys.stdin.readline().split()
t1 = int(t1)
t2 = int(t2)
count=0
for i in range(t1):
	num = int(input())
	if num%t2 == 0:
		count += 1
print(count) 
