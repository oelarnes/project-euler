# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

# We use our get_primes function. Since the sieve seems to be the best way to
# get primes and it requires storing all the primes, I don't see an advantage to
# looking for a more dynamic solution. We use a table of the pi function to estimate how 
# large a seive is needed. It looks like 200,000 should be sufficient. After running it 
# once, we reduced the estimate to only what is needed.

from prime_fact import get_primes

primes = get_primes(105000)

print primes[10000]

#104743