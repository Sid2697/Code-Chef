t=int(input())
for i in range(t):
	salary = int(input())
	if salary >= 1500:
		HRA = 500
		DA = 0.98*salary
		gross = salary+HRA+DA
		print(gross)
	else:
		HRA = 0.1*salary
		DA = 0.9 * salary
		gross = HRA+DA+salary
		print(gross) 
