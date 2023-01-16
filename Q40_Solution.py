#Q40
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910[1]112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the nth digit of the fractional part, find the value of the following expression.

d(1) × d(10) × d(100) × d(1000) × d(10000) × d(100000) × d(1000000)
'''

s = ['.']

checkers = 1000000

for x in range(1,checkers + 1):
    s.append(str(x))
d = ''.join(s)

keys = []
i = 1
answer = 1

for each in range(1,8):
    answer *= int(d[i])
    print(d[i])
    i *= 10
print(answer)