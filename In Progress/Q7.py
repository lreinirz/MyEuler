#ALRIGHT, HOW DO YOU FIND A PRIME NUMBER
prime_numbers_in_range = []


	#Should include 2, 3, 5, 7, 11, 13, 17, 19
def find_if_x_is_prime(tester):
	prime = []
	small_range = range(3, tester)
	for value in small_range:
		if tester % value == 0:
			prime.append(value)
	if len(prime) == 2:
		return True
	return False

testee = 0
while len(prime_numbers_in_range) < 10000:
	testee += 1
	for num in prime_numbers_in_range:
		if find_if_x_is_prime(testee) == True:
			prime_numbers_in_range.append(testee)

print(prime_numbers_in_range)
print(prime_numbers_in_range[-1])
