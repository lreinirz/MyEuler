'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True

def trunk_p(z):
    z = str(z)
    lenz = len(z)
    prime_check = None

    for it in range(lenz):
        prime_check = z[:it + 1]
        if prime_check == '1':
            return False
        if not is_prime(int(prime_check)):
            return False

    for it in range(lenz + 1):
        prime_check = z[-it:]
        if prime_check == '1':
            return False
        if not is_prime(int(prime_check)):
            return False
    return True

b = []
i = 8

while len(b) < 11:
    i += 1
    if is_prime(i):
        if trunk_p(i):
            print(i)
            b.append(i)
print(b)
print(sum(b))
