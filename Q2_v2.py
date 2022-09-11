previous, current, new, answer = 0, 1, 0, 0
#got dad's help with this one
while new < 4000000:
	new = current + previous
	previous = current
	current = new
	if new % 2 == 0:
		answer += new

print(answer)