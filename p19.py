# You are given the following information, but you may prefer to do some research 
# for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it
# is divisible by 400. How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

# Solution: Self-evident. 1 Jan 1901 was a Tuesday.

day = 2
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
count = 0
m_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in range(100):
	for month in range(12):
		#month == 0 sets day to the first of month 1, so count should be updated before
		#the change
		if day == 0:
			count += 1
		if year%4 == 3 and month == 1:
			day += 29 % 7
			day = day % 7
		else:
			day += m_length[month] % 7
			day = day % 7
			
print count