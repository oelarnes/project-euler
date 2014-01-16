# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
# without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers 
# from 1 to 20?

# Solution: We will use our prime factorization function, then find the minimal superset
# of the prime factorizations, with multiplicity. We will do this by defining a two-part
# union function for sorted lists.

from pe_functions import factor
from operator import mul

def pair_union(l1, l2):
# !!assumes sorted lists!!
	l = []
	while l1 != [] and l2 != []:
		e1 = l1.pop()
		e2 = l2.pop()
		if e1 == e2:
			l.insert(0, e1)
		if e1 > e2:
			l.insert(0, e1)
			l2.append(e2)
		if e2 > e1:
			l.insert(0, e2)
			l1.append(e1)
	return l1 + l2 + l
				
l = reduce(pair_union, [factor(j) for j in range(1,21)])
# print l
print reduce(mul, l, 1)

# Another solution: for each prime less than 20, list the highest power of that prime less 
# than or equal to 20, then take the product:
# 16, 9, 5, 7, 11, 13, 17, 19.
# Certainly faster.