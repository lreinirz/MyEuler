def factor_finder(digit):
                fac = [x for x in range(1, (digit // 2) + 1) if digit % x == 0]

                return fac

abundant = [x for x in range(28124) if sum(factor_finder(x)) > x]


cannot = [x for x in range(1, 24)]

for x in range(25, 28124):
                #Can x be the sum of two abundant numbers?
                for y in abundant:
                                #This goes through all abundant numbers
                                if x > y:
                                                dummy = x - y
                                if dummy not in abundant:
                                                cannot.append(x)
                                break
print(sum(cannot))




