# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# We count from the back until we get to an increase, recording the digits as we pass.
# When we get to a decrease, we increment that number from among the recorded digits,
# then append the rest into lexicographical order at the end.

from operator import add

def next_perm(perm):
	#in place
	tail = [perm.pop()]
	while perm != [] and tail[-1] < perm[-1]:
		tail.append(perm.pop())
	if perm == []:
		perm.extend(tail)
		return None
	for i, item in enumerate(tail):
		if item > perm[-1]:
			n = perm.pop()
			perm.append(tail[i])
			tail[i] = n
			perm.extend(tail)
			return None
	
perm = range(0,9)
for i in range(999999):
	next_perm(perm)

print reduce(add,[str(j) for j in perm])