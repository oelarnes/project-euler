# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


N = 28123

from pe_functions import proper_divs

def is_abundant(n):
	if sum(proper_divs(n)) > n:
		return True
	return False
	
abundants = []

for j in range(1,N+1):
	if is_abundant(j):
		abundants.append(j)

set_abundants = set(abundants)

sum = 0

for n in range(N,0,-1):
	j = 0
	done = False
	while not done:
		if abundants[j] > n/2:
			done = True
			sum += n
		elif n - abundants[j] in set_abundants:
			done = True
		else:
			j = j+1
				
print sum