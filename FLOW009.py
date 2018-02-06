import sys
def floating_decimals(f_val, dec):
    prc = "{:."+str(dec)+"f}" #first cast decimal as str
    #print(prc) #str format output is {:.3f}
    return prc.format(f_val)
t=int(input(''))
for i in range(t):
	n1,n2=sys.stdin.readline().split()
	quant=float(n1)
	price=float(n2)
	total=0
	if quant>1000:
		disc=price-0.1*price
		total = disc*quant
	else:
		total = price*quant
	print(floating_decimals(total, 6)) 
