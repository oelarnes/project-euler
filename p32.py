# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from operator import add

nums = [str(j) for j in range(1,10)]

def pandigital(*l):
	x = reduce(add, [str(n) for n in l])
	if all([s in x for s in nums]) and len(x) == 9:
		return True
	else:
		return False
	
pandigitals = []

for j in range(2,10):
	for k in range(1000,10000):
		if pandigital(j,k,j*k):
			pandigitals.append(j*k)
for j in range(10,100):
	for k in range(100,1000):
		if pandigital(j,k,j*k):
			pandigitals.append(j*k)
			
print sum([k for k in set(pandigitals)])