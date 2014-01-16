# Find a pythogorean triple a, b, c such that a + b + c = 1000

# Solution: c = 1000 - a - b, and wlog c > b > a > 0. The maximum value of a is below
# 332, and b ranges from a to 500 - a/2

from operator import mul
triples = []

for a in range(333):
	for b in range(a, 500 - a / 2):
		if a**2 + b**2 == (1000 - a - b)**2:
			triples.append([ a, b, 1000 - a - b ])
			
if triples == []:
	print "No triples found"
else:
	print reduce(mul, triples[0])