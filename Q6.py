sum_of_squares = 0
square_of_sum = 0
summ = 0
for x in range(1,101):
	sum_of_squares += x**2
	summ += x

square_of_sum = (summ**2)

print(square_of_sum - sum_of_squares)