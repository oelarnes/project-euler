# In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
# It is possible to make L2 in the following way:
# 
# 1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can L2 be made using any number of coins?

coins = [1,2,5,10,20,50,100,200]

def ways_to_make(n,coins):
	if coins == [1]:
		return 1
	if n == 0:
		return 1
	if n < 0:
		return 0
	return sum([ways_to_make(n-coin, coins[:j+1]) for j,coin in enumerate(coins)])
	
print ways_to_make(200, coins)