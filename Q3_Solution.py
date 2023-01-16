'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from time import process_time

critical = 600851475143 
useful = []

i = 1
while critical != 1:
	if critical % i == 0:
		critical = critical / i
		useful.append(i)
	i += 2

print(max(useful))

print("Process time: " + str(process_time() * 1000) + " ms.")
