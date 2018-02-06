t=int(input(''))
for i in range(t):
	code = input('')
	if code=='B'or code=='b':
		print('BattleShip')
	elif code=='C'or code=='c':
		print('Cruiser')
	elif code=='D'or code=='d':
		print('Destroyer')		
	elif code=='F'or code=='f':
		print('Frigate')
	else:
		print('You are gonna DIE') 
