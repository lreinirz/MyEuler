ran = range(1,21)
solution = None
divisor = 1
progress = []

while len(progress) < 20:
	for x in ran:
		if divisor % x == 0:
			progress.append(divisor)
		else:
			progress.clear()
			divisor *= 20
			x = 1
solution = divisor


print(solution)

#this takes a long time to get to an answer, mind you