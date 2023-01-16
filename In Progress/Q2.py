fibs = [1, 2]
x = 0
answer = 0

while fibs[-1] < 4000000:
	additional = int(fibs[-1]) + int(fibs[-2])
	fibs.append(additional)

print(answer)