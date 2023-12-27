'''
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0/1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d<1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

import decimal
from time import process_time

# AND I OWE IT ALL TO THIS NUMBER:
# 0.098711000955110009551100095511000955
# USED IT AS A TEST CASE


def is_recurring(i):
    #Reseting the context makes sure that the operation will list a very large number of decimal places
    context = decimal.Context(prec=9999, rounding=None, Emin=None, Emax=None, capitals=None, clamp=None, flags=None, traps=None)
    if i == 0:
        return False

    left = decimal.Decimal(1)
    right = decimal.Decimal(i)
    div = context.divide(left, right)
    #Above line is just 1/i

    if len(str(div)) < 9995:
        return False
    return str(div)


def find_sequence(x):
    '''
    One stop shop.
    "x" is the string version of the number being tested
    '''
    x = x.strip("0.")
    #Removes any 0s and demicals at the start and end of number. Can safely be removed.

    #If the first half of a number is the same as the second half of the number,
    #then it's the same number recurring all the way through.
    #It is not the answer. "1" can be returned and we can move on to the next number.
    if x[:int(len(x)/2)] == x[int(len(x)/2):]:
        return "1"


    current_ind = 0
    #Index of starting point. Will be increased if no matches.

    start = x[current_ind]
    #Selects a number; this is where the search for matching sequence begins
    #This will change at a later point. 

    next_ind_start = x.find(start, current_ind + 1)
    #Finds the next occurance of number selected by "current_ind"
    #next_ind_start is that number's index.

    start_seq = x[current_ind:next_ind_start]
#    print(f"Starting sequence is \n{start_seq}\nThis is perfect.")
    #A variable that contains all numbers between
    #"start" and the number at index "next_ind_start"

    start_seq_len = len(start_seq)
    #This is the leng of the above sequence,
    #start_seq

    next_ind_end = next_ind_start + start_seq_len

    next_seq = x[next_ind_start:next_ind_end]
#    print(f"Next sequence is {next_seq}")
    #Given the length of start_seq_len,
    #this variable contains all numbers after
    #the second occurance of the number selected in variable "start"
    #This is the same number of digits specified by
    #"start_seq" and "start_seq_len"

    current_ind = 0
    if next_ind_start == -1:
        next_ind_start = True
    while start_seq != next_seq:
#        print(f"Starting. Current index : {current_ind}, number is {x[current_ind]}")
        while next_ind_start:
            #Time to search for the next occurance of the number that corresponds with the starting index

            #"Find" is the correct function to use.
            #The second argument is where the search begins.

            #Essentially a repeat of the previous steps, using the next instance of the current_ind character found
            try:
                #If .index() can't find the stated number, it throws a ValueError.
                next_ind_start = x.index(start, next_ind_start + 1)

            except ValueError:
                next_ind_start = False
                #Setting it to false means it needs to be set as "True" to re-enter the cycle.
                break

            start_seq = x[current_ind:next_ind_start]
#            print(start_seq)
            start_seq_len = len(start_seq)
            next_ind_end = next_ind_start + start_seq_len
            next_seq = x[next_ind_start:next_ind_end]
#            print(next_seq)

            if start_seq == next_seq and start_seq:
                return start_seq

        current_ind += 1
        start = x[current_ind]
        next_ind_start = x.find(start, current_ind + 1)

        if next_ind_start == -1:
#            print("False flag")
            next_ind_start = False

    return start_seq

    

# x = "0.123456789012345678901"
# y = "0.1286666666666666666666666666667"



x = "0.098711000955110009551100095511000955"




x = "0.003333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"
# print(find_sequence(is_recurring(7)))


len_answer = 0
answer = 0
work_list = []

for x in range(2,1001):
    reoccurring = is_recurring(x)
    if reoccurring:
        work_list.append([reoccurring, x])



#recurring_list = [(is_recurring(each), each) for each in range(2, 1001) if is_recurring(1/each)]


for x in work_list:
    len_find_sequence = len(find_sequence(x[0]))
    if len_find_sequence > len_answer:
        len_answer = len_find_sequence
        answer = x[1]

print("Here it is:") 
print(f"Answer is {answer}, length of answer is {len_answer}")

print(find_sequence(is_recurring(983)))


print(f"Answer processed in {process_time() * 1000} milliseconds.")






# 1. Select next number in the sequence
# 2. Search for the next instance of that number
# 3a. If not found, break.
# 3b. If found, see what number comes after it
# 4. Compare the number following the found number, 
#    to the number following the "next" number
# 5a. If they match, extend both by 1
# 5b. If they don't match, skip to the next "found" number
# 5bi:Repeat until step 6 is reached (10 times?)
# 6. If they still match, extend the criteria for matching.
# 7. Continue extending until the end of the "next" sequence
#    reaches the beginning point of the "found" sequence
# 8. Count the length of the "next" sequence
# 9. If the length of the "next" sequence exceeds previous 
#    longest sequence, that's the current best answer
