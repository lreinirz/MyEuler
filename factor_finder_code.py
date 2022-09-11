import math

def factor_finder(q):
	'''Generates a list of factors for the number q'''
	factorA = []
	factorB = []
	sqrt = math.ceil(math.sqrt(q))

	for value in range(1, sqrt):
		if q % value == 0:
			factorA.append(value)
	for factor in factorA:
		z = q / factor
		factorB.append(int(z))
	factorB.sort()
	return factorA + factorB