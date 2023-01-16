from time import process_time
import math

def generate_triangle_numbers(n):
	'''Generates a list up to the 'n'th triangle numbers'''
	tnlist = []
	gen = 1
	dummy = 2
	while dummy <= n:
		tnlist.append(gen)
		gen += dummy
		dummy += 1
	return tnlist

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

tnl = 20000
list_of_possibles = generate_triangle_numbers(tnl)

for x in list_of_possibles:
	if len(factor_finder(x)) >= 500:
		print(x)
		break

print(f"I think the answer is {x}")

print("Process time: " + str(process_time()) + " seconds")