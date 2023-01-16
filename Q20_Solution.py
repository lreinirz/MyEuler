from time import process_time

multiple = 1
lists = []
summ = 0

for x in range(1,100):
	multiple *= x

lists = str(multiple)

for y in lists:
	summ += int(y)
print(summ)


print("Process time: " + str(process_time() * 1000) + "ms.")