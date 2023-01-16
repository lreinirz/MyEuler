from time import process_time

distinct_powers = []

def exp_comb(a,b):
	global distinct_powers
	for x in a:
		for y in b:
			distinct_powers.append(x ** y)
	return

o = range(2,101)
p = o
exp_comb(o, p)
distinct_powers = set(distinct_powers)
print(len(distinct_powers))

print("Process time: " + str(process_time() * 1000) + " ms.")