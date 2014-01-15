# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

# Solution:
#
# We simply do a calculation. The sum of the multiples of one less than n is
# n*(n-1)/2. The sum of the multiples of k less than n is k*(n/k * n/k-1)/2 (as integers).
# To find mutiples of 3 and 5, we use the inclusion exclusion principle.

# first attempt:
#
# print 3 * (1000/3) * (1000/3 - 1) / 2 + 5 * (1000/5) * (1000/5 - 1) / 2 - 15 * (1000/15) * \
#	(1000/15 - 1) / 2
	
# 233159

# second attempt:
# The calculation was correct in spirit but the formula was wrong

def sum_mult_k_below_n(k, n):
	return k * ( (n-1) / k + 1) * ( (n-1) / k ) / 2
	
print sum_mult_k_below_n(3, 1000) + sum_mult_k_below_n(5, 1000) - \
	sum_mult_k_below_n(15, 1000)
	
#233168