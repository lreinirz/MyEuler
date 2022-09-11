# The requirement is, basically, that you sum all this together, 
# then subtract duplicates, like multiples of both 3 and 5

from time import process_time

x = 0

while x*15 < 1000 or x*3 < 1000 or x*5<1000:
	x += 1
	fifteen = x * 15
	three = x * 3
	five = x * 5
	



print(f"The answer is {summation}")

print("Process time: " + str(process_time() * 1000) + " ms.")