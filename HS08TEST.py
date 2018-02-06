def solution():
    vals = input().split()
    withdraw, balance = float(vals[0]), float(vals[1])
    if withdraw % 5 == 0:
        withdraw += 0.5
        if balance - withdraw >= 0:
            balance -= withdraw
    print(format(balance, '.2f'))
 
solution()
