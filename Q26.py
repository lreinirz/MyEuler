# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1 

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

ran = range(1,1001)

def divider_form(value):
	return 1 / value

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

for x in ran:
	fraction_test = divider_form(x)
	fraction_string = str(fraction_test)
	if principal_period(fraction_string) != None:
		print(dict(x = principal_period(fraction_string)))


# 1. Find a way to divide 1 by all digits from 1 to 1000
# 2. Find a way to test for repeating sequence
# 3. Find a way to discover length of repeating sequence