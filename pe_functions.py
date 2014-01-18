import numpy

def get_primes(n):
	if n < 2:
		return []
	if n == 2:
		return [2]
	#lists primes up to and including n, since M could be exact
	primes = [2]
	nums = range(3, n+1, 2)
		# [3, 5, ... , n] ... nums[j] = 3 + 2*j, k = nums[(k-3)/2]
	j=0
	while nums[j]**2 <= n:
		# we remove odd multiples of nums[j] from nums[j]**2 up to int(M)
		if nums[j] > 0:
			for k in range(nums[j], n/nums[j]+1, 2):
				nums[( k*nums[j] - 3 ) / 2] = 0
		j = j + 1
	primes.extend(filter(None, nums))
		#those elements of nums that are non-0
	return primes

def factor(n):
	primes = get_primes(int(numpy.sqrt(n)))
	if n == 1:
		return []
	factors = [n]
	pop = True
	while (not pop and p<= numpy.sqrt(n)) or (primes != [] and primes[0]<= numpy.sqrt(n)):
		if pop:
			p = primes.pop(0)
		if not n%p:
			n = n / p
			factors.pop()
			factors.extend([p, n])
			pop = False
		else:
			pop = True
	return factors

def memoize(fn):
	cache = {}
	def newfn(*args):
		if args in cache:
			return cache[args]
		else:
			val = fn(*args)
			cache[args] = val
			return val
	return newfn

@memoize
def n_choose_r(n ,r):
	if n == r or r == 0:
		return 1
	else:
		return n_choose_r(n-1, r) + n_choose_r(n-1, r-1)

def factorial(n):
	if n == 0:
		return 1
	return n*factorial(n-1)
	
def merge_sort(l, greater):
	n = len(l)
	if n in [0, 1]:
		return l
	l1 = merge_sort(l[:n/2], greater)
	l2 = merge_sort(l[n/2:], greater)
	ls = []
	e1 = l1.pop(0)
	e2 = l2.pop(0)
	while True:
		if greater(e1, e2):
			ls.append(e2)
			if l2 == []:
				return ls + [e1] + l1
			e2 = l2.pop(0)
		else:
			ls.append(e1)
			if l1 == []:
				return ls + [e2] + l2
			e1 = l1.pop(0)
			
		
		
	