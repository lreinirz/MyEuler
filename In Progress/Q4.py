prime = []
ran = range(1,501)

for y in ran:
	for x in ran:
		if x % y != 0 and x > y and prime.count(x) == 0:
			prime.append(x)

print(prime)