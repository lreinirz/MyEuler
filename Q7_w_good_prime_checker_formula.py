'''
Q7.
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

#ALRIGHT, HOW DO YOU FIND A PRIME NUMBER

from math import floor

def prime_tester(i):
	'''
	improved code taken from Project Euler solution
	'''
	if i >= 10:
		if i % 2 == 0:
			return False
		elif i % 3 == 0:
			return False
		else:
			f = floor(i // 2)
				#square root of i
				#max factor
			line = 5

			while line <= f:
				if i % line == 0:
					return False
				elif i % (line + 2) == 0:
					return False
				line = line + 6
			return True

	else:
		if i <= 1:
			return False
		elif i < 4:
			return True
		elif i == 6 or i > 7:
			return False
		else:
			return True




for x in range(100):
	if prime_tester(x):
		print(x)

z = 1
testee = 1
while z < 10001:
	testee += 2
	if prime_tester(testee):
		z += 1
print(testee)


