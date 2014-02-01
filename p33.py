# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def cancel_digits(nums):
	#assume both two digit numbers
	n1, n2 = nums[0], nums[1]
	if str(n1)[0] == str(n2)[1]:
		nums[0] = int(str(n1)[1])
		nums[1] = int(str(n2)[0])
		return True
	if str(n2)[0] == str(n1)[1]:
		nums[0] = int(str(n1)[0])
		nums[1] = int(str(n2)[1])
		return True
	return False
	
for j in range(10,100):
	for k in range(j+1,100):
		if j != k:
			nums = [j,k]
			new_nums = nums[:]
			if cancel_digits(new_nums):
				if all(new_nums):
					if float(nums[ == float(nums[0])/float(nums[1]):
						print nums

# 100... need to fix code to reduce.						
						