'''
Reasonably efficient code 
for generating a list of primes 
up to the inputted upper limit

Scroll down for a duplicate of the code with explanations.
'''

def prime_list(upper_limit):
    '''
    Generates a list of prime numbers from 2 up to AND INCLUDING the upper limit
    '''
    primes = [2] + [x for x in range(3, upper_limit + 1, 2)]

    sqrt_limit = upper_limit**0.5

    sieve = [False for each in range(0, upper_limit + 1)]

    for n in range(4, upper_limit + 1, 2):
        sieve[n] = True

    for n in range(3, int(sqrt_limit) + 1, 2):
        if not sieve[n]:
            for i in range(n*n, upper_limit, 2 * n):
                sieve[i] = True

    return [2] + [x for x in range(3, upper_limit, 2) if not sieve[x]]
    


'''

def prime_list(upper_limit):
    primes = [2] + [x for x in range(3, upper_limit + 1, 2)]
        #adding 2 at the start, and then adding all numbers from 3 to 2,000,000 in
        #increments of 2, e.g. [5, 7, 9, etc]

    #2. Find the next number, "p", not crossed out. This is a prime. If this is greater than sqrt(upper_limit), we're done.
    sqrt_limit = upper_limit**0.5

    sieve = [False for each in range(0, upper_limit + 1)]
        #If false: number has either not been tested yet, or is prime

    for n in range(4, upper_limit + 1, 2):
        sieve[n] = True
        #all numbers from 4 to upper_limit that are even are now marked as True, and as such are not prime.
        #True stands for Composite numbers.

    for n in range(3, int(sqrt_limit) + 1, 2):
        #For each number in a range of odd numbers up to the square root of our upper limit:
        if not sieve[n]:
            print(n)
            #if the index of that number is False, then we have found the next Prime.
            for i in range(n*n, upper_limit, 2 * n):
                #for each number in the range of [prime number squared] up to [the upper limit], stepping by [prime * 2],
                #we know all numbers found here are not prime.
                #we know this because they are divisible by our prime number, as we are stepping through this list by the prime number 
                #e.g. if n is 7, and the upper limit is 100, then the values turned true would be:
                    #[49, 63, 77, 91], none of which are prime.
                #The reason we move forward by 2 * n is because if we only stepped by "n", we would hit an even number half the time
                    #e.g. [49, 56 which is even, 63, 70 which is even, 77, 84 which is even, 91, 98 which is even]
                    #That's inefficient

                sieve[i] = True
    for x in range(3, upper_limit, 2):
        if not sieve[x]:
            print(x)

    return [2] + [x for x in range(3, upper_limit, 2) if not sieve[x]]
        #compiles a list of numbers that are marked as "False" in the sieve
'''