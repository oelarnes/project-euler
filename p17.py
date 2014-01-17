# #If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
#  there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#  how many letters would be used?
# 
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
#  contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
#   "and" when writing out numbers is in compliance with British usage.

# Solution: Self-evident

digits = len('onetwothreefourfivesixseveneightnine')
tentonineteen = len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')
tens = len('twentythirtyfortyfiftysixtyseventyeightyninety')
hundred = len('hundred')
thousand = len('onethousand')
_and = len('and')

one_to_99 = digits+tentonineteen+10*tens+8*digits

print 100*digits + 900*hundred + 891*_and + 10*one_to_99 + thousand