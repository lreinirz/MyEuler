from time import process_time

def raiser(check):
	q = 0
	check = str(check)
	for x in check:
		q += int(x)**5
	if int(q) == int(check):
		return True
	return False

r = []
upper_bound = (9**5)*5


for x in range(2, upper_bound):
	if raiser(x):
		r.append(x)
print(sum(r))

print("Process time: " + str(process_time()) + " s.")