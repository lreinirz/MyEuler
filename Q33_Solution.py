#Q33
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from math import sqrt

numerator = 1
denomenator = 1
for n in range(11,100):
    if n % 10:
        for d in range(n + 1, 100):
            if d % 10:
                frac = n/d
                n_str, d_str = str(n), str(d)
                for num in n_str:
                    if num in d_str:
                        new_n = n_str.replace(num, "", 1)
                        new_d = d_str.replace(num, "", 1)

                        if float(new_n) * float(new_d) == 0:
                            break
                        elif float(new_n) / float(new_d) == 1:
                            break
                        elif float(new_n)/float(new_d) == frac:
                            print(n_str, "/", d_str)
                            numerator *= n
                            denomenator *= d
                            break

def gcf(first, second):
    def factorize(x):
        factors = []
        x = int(x)
        for i in range(1,int(sqrt(x)) + 1):
            if x % i == 0:
                factors.append(i)
        for each in factors[::-1]:
            factors.append(int(x/each))
        return factors
    n_fact = factorize(first)
    d_fact = factorize(second)
    gcf_list = sorted([x for x in n_fact if x in d_fact])

    return gcf_list[-1]

answer = int(denomenator/gcf(numerator, denomenator))
print(f"Answer: {answer}")