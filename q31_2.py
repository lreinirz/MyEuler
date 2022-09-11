from math import floor

coins = [1,2]
goal = 5

def fworkingmax(l):
    '''This removes the largest value in the passed in list
    and returns the removed value
    Returns False if list is empty'''
    try:
        current_max = max(l)
        i_current_max = l.index(current_max)
        working_max = l.pop(i_current_max)

        return working_max

    except ValueError:
        return False

def combo_count(lcoin, goal):
    combo_count = 0
    unused = lcoin
    used = []

    while len(lcoin) != 0:
        current_max = fworkingmax(lcoin)
        initial_multiplier = floor(goal/current_max)
        print(initial_multiplier)
#        print("Goal", goal, "current_max", current_max, "initial_multiplier", initial_multiplier)

        while initial_multiplier > 0:
            residual = goal - (initial_multiplier*current_max)
            initial_multiplier -= 1

            if residual == 0:
                combo_count += 1
                #because we have found a combo that sums to goal
                residual = 1

    return combo_count


def max_list(l):
    '''Returns the maximum in a list
    And returns a list without the maximum'''
    mlist = l
    m = max(l)
    mlist.remove(m)
    return m, mlist

#Current goal:
#Have the computer figure out how many ways a 1p coin can make 1p


z = combo_count(coins, goal)
print("Answer is", z)

j = [1,2,3,4,5,6,7,8]
print(max_list(j))
a, b = max_list(j)
print(a)
print(b)


    # combo_count = 0
    # unused = lcoin
    # used = []


