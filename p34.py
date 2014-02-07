# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# Solution: We have to find an upper bound. 9! = 362880, so a 7 digit number < 362880*7 =
# ~ 2500000, which has at most 5 9's, so the actual maximum is 362880*5 ~ 1800000. First
# we check with brute force, otherwise, strict assumptions can be made about the digits 
# of large numbers that heavily reduce the computation time.

import math

def digify(n):
	return [int(letter) for letter in str(n)]
	
fact = [math.factorial(j) for j in range(10)]

s = 0
	
for j in range(3, 2000000):
	if sum([fact[digit] for digit in digify(j)]) == j:
		s += j
		
print s