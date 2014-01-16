# Find the difference between the sum of the squares of the first one hundred natural 
# numbers and the square of the sum.

# Solution: The difference reduces to 2 sum(n_i * n*j) for i > j over the set in question.
# We can factor n_j out and sum using triangular identity.

N = 100

print sum([j*(N*(N+1) - j*(j+1)) for j in range(1, N+1)])

# there exist identities for these sums as well, if a closed formula is desired.

# 25164150