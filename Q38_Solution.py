#Q38
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

#I know the maximum has to be under 10,000, because 10000 times 1 concatenated with 10000 times 2 is 1000020000, which is 10 characters long.
#Therefore, it cannot be pandigital, as it has more than the nine numbers in it, 123456789.

def pandigital(num):
    r = '123456789'
    num = str(num)

    for char in r:
        if char not in num:
            return False
    return True

largest = 0

for run in range(1,9999):
    dummy = 0
    cat = ""
    while len(cat) < 8:
        dummy += 1
        cat += str(dummy *run)
    if len(cat) > 9:
        pass
    elif pandigital(cat):
        if int(cat) > int(largest):
            largest = cat
            print(cat)
            print(run)
print("Answer: " + largest)