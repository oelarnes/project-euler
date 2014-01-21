# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Solution: Based on the observation that the upper-right corner of each square is (2 * k + 1)**2, we find that the sum of the four corners of each square past the first is given by the formula S_k = 16 * k**2 + 4 * k + 4. Where k = 1 is the first square around the 1. A (2n - 1) x (2n - 1) grid has squares for k from 0 to n - 1, so we get:

print 1 + sum([16 * k**2 + 4 * k + 4 for k in range(1, 501)])

# 669171001