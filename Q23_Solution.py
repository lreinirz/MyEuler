'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1+2+4+7+14 = 28, which means that 28 is a perfect number.

A number N is called deficient if the sum of its proper divisors is less than N,
and it is called abundant if this sum exceeds N.

As 12 is the smallest abundant number, 1+2+3+4+6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis,
 even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers 
 is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from functools import reduce

def factorize(n):
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))

def proper_divisors(n):
    #The only difference between this and factorize()
    #is that this one doesn't include n in the returned set.
    #This is done by having the range exclude 1, and adding it 
    #to the listafter the list of factors have been generated
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if not n % i), [1]))    

def abundant_number(ulim):
    return [num for num in range(ulim + 1) if sum(proper_divisors(num)) > num]


abundance = abundant_number(28123)
# print("this one:")
# print(len(abundance))
# print(abundance[-1])

print("WRONG ANSWER")
upper_range = 28124
proper_abundance = abundant_number(upper_range)


summed_abundance = set([x+y for y in proper_abundance for x in proper_abundance if x + y <= 28123])

answer_list = [x for x in range(upper_range) if x not in summed_abundance]

answer = sum(answer_list)

print(answer)

print(4179871 - answer)
print(995 in answer_list)


print("RIGHT ANSWER")
upper_range = 28124
proper_abundance = abundant_number(upper_range)
#this step made the difference:
proper_abundance.pop(0)

summed_abundance = set([x+y for y in proper_abundance for x in proper_abundance if x + y <= 28123])

answer_list = [x for x in range(upper_range) if x not in summed_abundance]

answer = sum(answer_list)

print(answer)

print(4179871 - answer)
print(995 in answer_list)
