def factorial(n):
    answer = 1
    while n >= 1:
        i = n
        n = n - 1
        answer *= i
    if n == 1:
        return 1
    return answer

def f_summer(q):
    q = str(q)
    obsolete = 0
    for num in q:
        num = int(num)
        obsolete += factorial(num)
    if int(obsolete) == int(q):
        print(obsolete)
        return True
    else:
        return False

answer = 0
for x in range(3, 100000):
    if f_summer(x):
        answer += x

print(f'The answer is {answer}')
