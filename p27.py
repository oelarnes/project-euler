# Euler discovered the remarkable quadratic formula:
# 
# n**2 + n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.
# 
# 
# Considering quadratics of the form:
# 
# n**2 + an + b, where |a| < 1000 and |b| < 1000
# 
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

# Solution: 

# Guessing that the correct formula is a shift of the other two. The general formula is n**2 - (2*k - 1)*n + 41 + k**2 - k, solve for largest k such that 41 + k**2 - k < 1000:

k = max([k * (41 + k**2 - k < 1000) for k in range(40)])

a = 1 - 2 * k 
b = 41 + k**2 - k

print a*b