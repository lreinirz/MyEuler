from time import process_time

def proper_divisors(whole):
	div_list = []
	for x in range(1, whole):
		if whole % x == 0:
			div_list.append(x)

	return div_list

q = []
r = []
for value in range(1, 10001):
	if sum(proper_divisors(sum(proper_divisors(value)))) == value:
		q.append(value)

for x in q:
	if sum(proper_divisors(x)) == x:
		r.append(x)

answer = sum(q) - sum(r)

print(f"The answer is {answer}")

print("Process time: " + str(process_time() * 1000) + " ms.")