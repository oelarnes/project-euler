# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which 
# divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each
# of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
# so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

# Solution: We calculate the sum of proper divisors using previous methods
# and make a pass through the array of values. There are probably ways to make this 
# faster but it doesn't seem necessary. Amicable numbers are still amicable if we include
# all divisors.

from pe_functions import factor
from operator import mul

N = 10000

def key_increment(key, max):
	n = len(max)
	for j in range(n):
		if key[j] < max[j]:
			key[j] += 1
			return None
		else:
			key[j] = 0

div_sums = [0]*(N-1)
for k in range(2,N):
	sum = 0
	p_fact = factor(k)
	s = {}
	for el in p_fact:
		if el not in s:
			s[el] = 1
		else:
			s[el] += 1
	vals = [s[el] for el in s]
	primes = [el for el in s]
	key = [0]*len(vals)
	while key != vals:
		sum += reduce(mul, [primes[j]**key[j] for j in range(len(vals))], 1)
		key_increment(key, vals)
	div_sums[k-1] = sum

sum = 0	
for j in range(N-1):
	if div_sums[j] < N:
		if div_sums[div_sums[j]-1] == j+1 and div_sums[j] != j+1:
			sum += j+1
			#print j+1

print sum