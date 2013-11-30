# (e)

validName = False # assume invalid input for desired username

while not validName:
    targetName = str(input('Enter username of desired player: '))
    if len(targetName) > 10:
        print('Username has to be under 10 characters.')
    else:
        validName = True

with open('Players.dat', 'r') as infile:
    found = False # assume target player not yet found
    while not found:
        player = infile.readline()
        if player == '': # target player not found
            print('Entered username not found in list of players.')
            break
        else:
            player1 = player.rsplit(', ')
            if player1[0] == targetName:
                print('Score of player ' + targetName + ' is ' + player1[1][:-1] + '.')
                found = True

infile.close()    
