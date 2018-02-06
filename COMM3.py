import math
def dist(x1,y1,x2,y2):
	distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
	return distance
import sys
t=int(input(''))
for i in range(t):
	max=int(input(''))
	C1x,C1y=sys.stdin.readline().split()
	C1x=int(C1x)
	C1y=int(C1y)
	C2x,C2y=sys.stdin.readline().split()
	C2x=int(C2x)
	C2y=int(C2y)
	C3x,C3y=sys.stdin.readline().split()
	C3x=int(C3x)
	C3y=int(C3y)
	D1_2=dist(C1x,C1y,C2x,C2y)	#Distance Between Chef 1 and 2		
	D1_3=dist(C2x,C2y,C3x,C3y)	#Distance Between Chef 1 and 3		
	D3_2=dist(C3x,C3y,C1x,C1y)	#Distance Between Chef 2 and 3
	#print(max,D1_2,D1_3,D3_2)		
	if (D1_2 <= max and D3_2 <= max) or (D1_2 <= max and D1_3<=max) or (D3_2<=max and D1_3<=max):
		print('yes')
	else:
		print('no') 
