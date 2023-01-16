r = range(20, 0, -1)
z = 1
for each in r:
	z *= each
print(z)
solution = None
divisor = 1
progress = []

while len(progress) < 20:
	for x in r:
		if divisor % x == 0:
			progress.append(divisor)
		else:
			progress = []
			divisor *= 20
			x = 1
solution = divisor


print(solution)

#this takes a long time to get to an answer, mind you