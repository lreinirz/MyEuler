'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

prime = []
ran = range(100,1000)

for y in ran:
	for x in ran:
		if x % y != 0 and x > y and prime.count(x) == 0:
			prime.append(x)

print(prime)