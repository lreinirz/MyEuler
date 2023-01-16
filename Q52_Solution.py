#q52
'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

answered = False

def num_in_multi(i, multiples):
    for run in range(2, multiples + 1):
        dummy = str(i * run)
        for char in str(i):
            if char not in dummy:
                return False
        for char in dummy:
            if char not in str(i):
                return False
    return True

x = 0

while not answered:
    x += 1
    if num_in_multi(x, 6):
        answered = True
        print("Answer: " + str(x))
