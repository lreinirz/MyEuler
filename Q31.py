#alright let's try 5s

from math import floor

coins = [1, 2, 5, 10, 20, 50, 100, 200]

combo_count = 0

mini_count = [1,2]

#issue with... initial multiplier
#and current max

def fworkingmax(l):
    '''This removes the largest value in the passed in list
    and returns the removed value'''

    current_max = max(l)
    i_current_max = l.index(current_max)
    working_max = l.pop(i_current_max)

    return working_max


def sum_count(lcoin, goal):
    '''lcoin is list of coin values
    goal is the value we're summing to get to'''
    initial_multiplier = 2
    combo_count = 0

    while len(lcoin) > 0:
        print(f"len(lcoin): {len(lcoin)}")
        current_max = fworkingmax(lcoin)
        initial_multiplier = floor(goal/current_max)
        print("cm", current_max, "im", initial_multiplier)

        while initial_multiplier > 0:
            print(initial_multiplier)
            residual = goal - (initial_multiplier*current_max)
            initial_multiplier -= 1
            if residual == 0:
                combo_count += 1
                #because we have found a combo that sums to goal
                residual = 1

            while residual != 0:
                if lcoin:
                    print(f"len(lcoin) the second: {len(lcoin)}")
                    secondary_list = lcoin
                    secondary_max = fworkingmax(secondary_list)


                print("goal", goal, "initial multiplier:", initial_multiplier, "current_max:", current_max)

                residual = goal - (initial_multiplier*secondary_max)
                print(f"residual is {residual}")


                if residual == 0:
                    combo_count += 1
                    print("step 8")
                        #because we have found a combo that sums to goal
                residual = 0

    return combo_count

#we want to find the combinations that equal 5
goal = 5

answer = sum_count(mini_count, 2)
print("Answer is ", answer)





# current_max = fworkingmax(mini_count)

# initial_multiplier = floor(goal/current_max)
#this would return 1, with the max being 5


# residual = goal - (initial_multiplier*current_max)
#while residual != 0, we will continue with the current max
#in this case, the current max has fulfilled its function. 
#The multiplier can now be reduced by 1. 
#Once the multipler hits 0, we can move on to the next maximum
    #The next step in this project is to iterate off this so goal is 10


#now i want that initial multipler to:
#1. multiply by the max, see what's left
#2. reduce by 1
#3. the goal can then be replaced by the new maximum
#4. now that we have solved that maximum










def combo_sum_counter(coin_list, goal):

    current_max = max(coin_list)
    initial_multiplier = floor(goal/current_max)

    while count < goal:
        pass