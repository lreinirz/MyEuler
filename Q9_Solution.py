'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def square_sum(base1, base2):
    return base1 ** 2 + base2 ** 2


for x in range(1001):
    for y in range(1001):
        if x < y and square_sum(x, y) ** .5 + x + y == 1000:
            print(int(x * y * square_sum(x, y) ** .5))

'''
Alternate solution:
'''
from math import sqrt

i = 1 
squares = []
while i <= 1000:
    squares.append(i**2)
    i += 1

answer = False
while not answer:
    for b2 in squares:
        if answer:
            break
        for a2 in squares:
            if a2 >= b2:
                break
            else:
                c2 = a2 + b2
                if c2 in squares:
                    a, b, c = sqrt(a2), sqrt(b2), sqrt(c2)

                    if a + b + c == 1000:
                        answer = a*b*c
                        print(a,b,c)
                        break

print(f"Answer: {int(answer)}")