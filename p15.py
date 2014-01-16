# Starting in the top left corner of a 2x2 grid, and only being able to move to the right
#  and down, there are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20x20 grid?from pe_functions import n_choose_r

# Solution: The number of such paths is 2n choose n. We implement this function
# dynamically.

from pe_functions import memoize

@memoize
def n_choose_r(n ,r):
	if n == r or r == 0:
		return 1
	else:
		return n_choose_r(n-1, r) + n_choose_r(n-1, r-1)

print n_choose_r(40,20)