'''
Q10.
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

''' 
Solution explanation:
I'm going to make a version of the Sieve of , which can be stated in the following steps:
1. Make a list of all numbers from 2 to N.
2. Find the next number p not yet crossed out. This is a prime.
If it is greater than √N, go to 5.
3. Cross out all multiples of p which are not yet crossed out.
4. Go to 2.
5. The numbers not crossed out are the primes not exceeding N.
'''
from time import process_time

#1. Make a list of all numbers from 2 to N, with N being 2,000,000
N = 2000000
sieve_list = [2] + [x for x in range(3, N + 1, 2)]
    #adding 2 at the start, and then adding all numbers from 3 to 2,000,000 in
    #increments of 2, e.g. [5, 7, 9, etc]

#2. Find the next number, "p", not crossed out. This is a prime. If this is greater than sqrt(N), we're done.
sqrt_limit = N**0.5
    #sqrt(2000000)

answer = 0

sieve = [False for each in range(0, N + 1)]
    #If false: number has either not been tested yet, or is prime

for n in range(4, N + 1, 2):
    sieve[n] = True
    #all numbers from 4 to 2,000,000 that are even are now marked as True
    #True stands for Composite numbers.

for n in range(3, int(sqrt_limit) + 1, 2):
    #For each number in a range of odd numbers up to the square root of our upper limit:
    if not sieve[n]:
        #if the index of that number is False, then we have found the next Prime.
        for i in range(n*n, N, 2 * n):
            #for each number in the range of [prime number squared] up to [the upper limit], stepping by [prime * 2],
            #we know all numbers found here are not prime.
            #we know this because they are divisible by our prime number, as we are stepping through this list by the prime number 
            #e.g. if n is 7, and the upper limit is 100, then the values turned true would be:
                #[49, 63, 77, 91], none of which are prime.
            #The reason we move forward by 2 * n is because if we only stepped by "n", we would hit an even number half the time
                #e.g. [49, 56 which is even, 63, 70 which is even, 77, 84 which is even, 91, 98 which is even]
                #That's inefficient

            sieve[i] = True

for z in range(2, N):
    if not sieve[z]:
        answer += z

print(answer)

print("Process time: " + str(process_time() * 1000) + " ms.")