# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

# Solution: we create a hash table of primes rotated to their lowest position. At the end
# we search the table for keys with a number of values equal to the number of digits

# This misses 11! We did not account for primes that are self rotations. Also miscounted
# primes with the digit '0'. Our solution is hacky but works.

from pe_functions import get_primes

def lex_lowest_rotation(n):
	# uses the fact that string comparisons are lexicographical
	word = str(n)
	lowest = word
	n = len(word)
	for j in range(n-1):
		word = word[n-1] + word[:n-1]
		if word < lowest:
			lowest = word
	return int(lowest)
	
catalogue = {}

for prime in get_primes(1000000):
	# exclude primes with zeros, they can't be solutions anyway
	if '0' not in str(prime):
		rotation = lex_lowest_rotation(prime)
		if rotation in catalogue:
			catalogue[rotation] += 1
		else:
			catalogue[rotation] = 1

num = 0

for key in catalogue:
	num_rots = 1
	key_str = str(key)
	n = len(key_str)
	word = key_str
	for j in range(n-1):
		next = word[n-1] + word[:n-1]
		if next == key_str:
			num_rots += 1
	if catalogue[key] == len(str(key)) - num_rots + 1:
		num += catalogue[key]
		
print num

# 55
		