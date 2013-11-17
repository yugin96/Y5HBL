# (c)

# random number generator to generate 5000 usernames and scores

# generate username: generate random decimal number and convert to ASCII
# alphanumeric character

import sys
sys.setrecursionlimit(10000)

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
    for j in range(name_length - 1):
        valid_num = False # assume randomly generated number is invalid
        while not valid_num:
            randnum = random.randrange(48, 123)
            if (randnum <= 57) or (65 <= randnum <= 90) or (randnum >= 97):
               valid_num = True
        username = username + str(chr(randnum))
    score = random.randrange(0, 100000)
    players.append([username, score])

# modified binary sort to sort according to score first, before sorting
# players with identical scores by alphabetical order

def quicksort(elements):
    if elements == []:
        return []
    else:
        pivot = elements[0]
        pivot1 = elements[0][1]
        less, greater = [], []
        for element in elements:
            if element[1] > pivot1:
                greater.append(element)
            else:
                less.append(element)
        return quicksort(greater) + [pivot] + quicksort(less)

print(quicksort(players))
    
    
    
    
