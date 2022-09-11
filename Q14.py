def collatz_string_length(value):
	collatz_string = []
	while value != 1:
		collatz_string.append(value)
		if value % 2 == 0:
			value = value / 2
		else:
			value = (value * 3) + 1
	return len(collatz_string)


ran = range(1,1000000)
answer = []

for x in ran:
	answer.append(collatz_string_length(x))
	#for any n, if the length has already been done, 
	#then that can be referred to again 
print(answer.index(max(answer)))