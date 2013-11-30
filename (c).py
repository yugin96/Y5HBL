# (c)

# random number generator to generate 5000 usernames and scores

# generate username: generate random decimal number and convert to ASCII alphanumeric
# alphanumeric character if possible; if not, generate another number

players = [] # initialise array for holding player date

import random

for i in range(5000): # generate 5000 username-score pairs
    name_length = random.randrange(5, 11) # generate 5-10 character-long usernames
    username = '' # initialise empty string for username
    valid_num = False # assume randomly generated number is invalid
    while not valid_num:
        randnum = random.randrange(48, 123)
        if (65 <= randnum <= 90) or (randnum >= 97): # first character must be alphabet
           valid_num = True
    username = username + str(chr(randnum))
    for j in range(name_length - 1):
        valid_num = False # assume randomly generated number is invalid
        while not valid_num:
            randnum = random.randrange(48, 123)
            if (randnum <= 57) or (65 <= randnum <= 90) or (randnum >= 97):
               valid_num = True
        username = username + str(chr(randnum))
    score = random.randrange(0, 100000)
    players.append([username, score])

# modified binary sort to sort according to score first, before sorting players
# with identical scores by alphabetical order

def quicksort(elements):
    if elements == []:
        return []
    else:
        pivot = elements[0]
        pivot1 = elements[0][1]
        less, greater = [], []
        for element in elements[1:]:
            if element[1] > pivot1:
                greater.append(element)
            elif element[1] < pivot1:
                less.append(element)
            else: # scores are equal
                sort = False # assume not sorted
                i = 0
                while not sort:
                    if ord(element[0][i]) > ord(pivot[0][i]):
                        less.append(element)
                        sort = True
                    elif ord(element[0][i]) < ord(pivot[0][i]):
                        greater.append(element)
                        sort = True
                    else:
                         i += 1                                 
        return quicksort(greater) + [pivot] + quicksort(less)

sortedPlayers = quicksort(players)

with open('players.dat', 'w') as outfile:
    for player in sortedPlayers:
        outfile.write(player[0] + ', ' + str(player[1]))
        outfile.write('\n')
    outfile.close()
    
    
