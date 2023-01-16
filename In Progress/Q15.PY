#You need to build pascal's triangle
#The middle number of the 3rd row corresponds to the number of lattice paths for a 1x1 cube
#The middle number of the 5th row corresponds to the number of lattice paths for a 2x2 cube
#The middle number of the 7th row corresponds to the number of lattice paths for a 3x3 cube
#So the middle number of the something-th row corresponds to the number of lattice paths for a 20x20 cube

#I made something that generates Pascal's triangle to the nth row
#I also made a shitty program that tells me how many rows are needed for a 20x20 because math

def pascal(number_of_rows_requested, last_only = False):
    starters = [[1],[1, 1]]
    number_of_rows_requested -= 2

    for request in range(0, number_of_rows_requested):
        #The above line is fine. 


        new_row = [sum(starters[-1][x : x + 2]) for x in range(0, len(starters[-1]))]
        new_row.insert(0, 1)
        # new_row.append(1)

        #For the first row, it's going once, then twice.
        # print(sum(starters[-1][x : x + 2]))

        starters.append(new_row)
    if last_only == False:
        return starters
    return starters[-1]



#Row 1 == 0x0, 
#Row 3 == 1x1,
#Row 5 == 2x2 
#Row 7 == 3x3





def fuck_it(how_many):
    row = 1
    squares = 0
    for x in range(0, how_many):
        row += 2
        squares += 1
    return row


final = pascal(fuck_it(20), True)
print(f"The answer is {final[int((len(final) -1 ) / 2)]}")



