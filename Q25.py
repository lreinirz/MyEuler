fibonacci_list = [1,1]
fibonacci_string = ["1", "1"]
next_value = 0

while len(fibonacci_list) <= 5000:
	while len(fibonacci_string[-1]) < 1000:
		next_value = fibonacci_list[-1] + fibonacci_list[-2]
		fibonacci_list.append(next_value)
		fibonacci_string.append(str(next_value))
	break
print(fibonacci_string.index(fibonacci_string[-1]) + 1)