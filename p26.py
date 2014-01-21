# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# Solution. Let d = 2^j*5^k*m, where m is mutually prime to 2 and 5. Then let p = max(j, k) (say k>j), and 10^d / d = 2^(k-j)/m. Since we know rational numbers have repeating decimals, m must divide some 10^q - 1 evenly. The smallest such q then is what we are looking for. To save time, we need only check numbers relatively prime to 2 and 5, since for any number with q repeating digits, we have already checked m which also has q repeating digits.

q_best = 6
d_best = 7

for j in range(11,1000):
	if j%2 and j%5:
		done = False
		m = 1
		while not done:
			if not (10**m - 1) % j:
				if m > q_best:
					q_best = m
					d_best = j
				done = True
			m += 1
			
# def q(m):
# 	n = 1
# 	while True:
# 		if not (10**n - 1) % m:
# 			return n
# 		n += 1

print d_best

# 983

# The answer suggests Fermat's little theorem, since 1/983 has 982 digits. Recall that a^(p-1) = 1 mod p for all primes p.