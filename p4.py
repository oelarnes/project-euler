# A palindromic number reads the same both ways. The largest palindrome made from the 
# product of two 2-digit numbers is 9009 = 91 x 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

# Solution:
# We write a palindrome checked and use brute force.
import numpy

def convert_to_list(n):
	l = []
	exp = int(numpy.log10(n))
	for j in range(exp+1):
		l.insert(0, (n / 10**j) % 10)
	return l
		
def is_palindrome_list(l):
	for j in range(len(l)/2):
		if l[j] != l[-j-1]:
			return False
	return True
	
def is_palindrome(n):
	return is_palindrome_list(convert_to_list(n))

best = 0

for j in range(100, 1000):
	for k in range(j, 1000):
		if is_palindrome(j*k) and j*k > best:
			best = j*k
			
# print is_palindrome(5)
# print is_palindrome(45)
# print is_palindrome(454)
# print is_palindrome(395093845)
# print is_palindrome(123454321)
# print is_palindrome(12344321)
		
print best