'''
Q35.
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from math import sqrt

def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2, int(sqrt(n))+1):
        if (n % i) == 0:
            return False

    return True

def rotate_prime(x):
    x = str(x)
    for each in range(len(x)):
        if not is_prime(int(x)):
            return False
        x = x[1:] + x[0]
    return True



values = [2,]
for x in range(3, 1000001, 2):
    if is_prime(x):
        if rotate_prime(x):
            values.append(x)
print(values)
print(len(values))
