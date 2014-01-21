# The Fibonacci sequence is defined by the recurrence relation:
# 
# Fn = Fn-1 + Fn-2
# Hence the first 12 terms will be:
# 
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the first term (what is the index of the first term) in the Fibonacci sequence to contain 1000 digits?

from math import log10

f_n = 1
f_nplus1 = 1

n=2

while int(log10(f_nplus1)) < 999:
	f_nplus1 = f_nplus1 + f_n
	f_n = f_nplus1 - f_n
	n += 1
	
print n

# 4782