t=int(input())
for i in range(t):
	hard,carb,tens = input().split()
	hard,carb,tens = [int(hard),float(carb),int(tens)]
	if hard > 50 and carb < 0.7 and tens > 5600:
		print('10')
	elif hard > 50 and carb < 0.7 and tens <= 5600:
		print('9')		
	elif tens > 5600 and carb < 0.7 and hard <= 50 :
		print('8')		
	elif hard > 50 and tens > 5600 and carb >= 0.7:
		print('7')
	elif hard > 50 or carb < 0.7 or tens > 5600:
		print('6')
	else:
		print('5')
