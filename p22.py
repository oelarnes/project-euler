# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
# 
# What is the total of all the name scores in the file?

# Solution: We implement merge_sort to sort the names, passing in the list of names
# and a comparison function, returning the sorted list. Calculating the values is straightforward after that.

import string
from pe_functions import merge_sort

key = {}
for j in range(26):
	alpha = string.ascii_uppercase
	key[alpha[j]] = j+1
	
def greater(name1, name2):
	n1 = len(name1)
	n2 = len(name2)
	for j in range(max(n1, n2)):
		if n1 == j:
			return False
		if n2 == j:
			return True
		if key[name1[j]] > key[name2[j]]:
			return True
		if key[name2[j]] > key[name1[j]]:
			return False
	return False

f = open("names.txt", 'r')

names = f.read()

name_list = [string.strip(name, '"') for name in names.split(',')]

name_list = merge_sort(name_list, greater)


total = 0
n = 1
for name in name_list:
	total += n*sum([key[letter] for letter in name])
	n += 1

print total

# 871198282