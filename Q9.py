def square_sum(base1, base2):
    return base1 ** 2 + base2 ** 2


for x in range(1001):
    for y in range(1001):
        if x < y and square_sum(x, y) ** .5 + x + y == 1000:
            print(int(x * y * square_sum(x, y) ** .5))
