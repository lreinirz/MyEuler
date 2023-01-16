'''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

#I know that any number whse digits add up to a number divisible by three is, itself, divisible by three
#e.g. 692187; 6+9+2+1+8+7 = 33, 33 % 3 == 0. 692187 / 3 = 230,729.
#Therefore, any eight or nine digit number with 1-8 or 1-9 in it will also be divisible by 3, and thus is not prime.
#1+2+3+4+5+6+7+8 = 36; 36+9 = 45. 3+6 = 9, % 3 == 0; 4 + 5 = 9, % 3 == 0 
#So we know that the highest number to start with would be 7654321, and we can go down from there. 
#This saves several million steps. 

from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True

x = 7654321

while True:
    counter = 0
    x -= 2
    if is_prime(x):
        s = str(x)
        for each in range(1, len(s) + 1):
            if str(each) not in s:
                break
            else:
                counter += 1
        if counter == len(s):
            print(f"Answer: {s}")
            break


