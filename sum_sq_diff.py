# Find the difference between the sum of the squares of the first one hundred natural 
# numbers and the square of the sum.

# Solution: The difference reduces to 2 sum(n_i * n*j) for i > j over the set in question

N = 100

ar = [[j*k for j in range(k+1, N+1)] for k in range(1, N+1)]

s = 2*sum([sum(l) for l in ar])

print s