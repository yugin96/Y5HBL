# (j)

end = False # assume player has not exited menu

while not end:
    print('Menu:')
    print('a) Add username and score of a new player to leaderboard.')
    print("b) Find a player's score based on his/her username.")
    print('c) Generate list of usernames of players with the same score.')
    print('d) Generate list of usernames and scores of players within five ranks of a given score.')
    print('e) Generate list of usernames and scores of the five players ranked above and below a player with a particular score.')
    choice = input('Enter the letter corresponding to the option you wish to choose: ')

    if choice == 'a':
        import random

        validName, validScore = False, False # assume invalid inputs for new player's data

        while not validName:
            newUsername = str(input('Enter username of new player: '))
            if len(newUsername) > 10:
                print('Username has to be under 10 characters.')
            else:
                validName = True

        while not validScore:
            newScore = int(input('Enter score of new player: '))
            if newScore < 0:
                print('Value too low. Score must be from 0 to 99999.')
            elif newScore > 99999:
                print('Value too high. Score must be from 0 to 99999.')
            else:
                validScore = True

        # read scores from original 'Players.dat' file, write updated list of scores
        # to 'PlayersNew.dat' file.

        infile = open('Players.dat', 'r')
        outfile = open('PlayersNew.dat', 'w')

        added = False # assume new player not yet added into data file
        while not added:
            player = infile.readline()
            score = int((player.rsplit(', '))[1])
            if score > newScore:
                outfile.write(player)
            elif score < newScore:
                outfile.write(newUsername + ', ' + str(newScore))
                outfile.write('\n')
                outfile.write(player)
                added = True
            else: # currently read score and new score are equal
                alpha = False # assume alphabetical order not yet determined
                i = 0
                while not added1:
                    if ord(player[i]) < ord(newPlayer[0][i]):
                        outfile.write(player)
                        alpha = True
                    elif ord(player[i]) > ord(newPlayer[0][i]):
                        outfile.write(newPlayer[0] + ', ' + str(newPlayer[1]))
                        outfile.write('\n')
                        outfile.write(player)
                        alpha = True
                    else:
                        i += 1
                added = True
        EoF = False # assume not end of file
        while not EoF:
            player = infile.readline()
            if player != '':
                outfile.write(player)
            else:
                EoF = True

        infile.close()
        outfile.close()

        end = input('Operation successful. Would you like to continue? (Y/N): ')
        if input == 'N':
            end = True

    elif choice == 'b':
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

        choice = input('Operation successful. Would you like to continue? (Y/N): ')
        if choice == 'N':
            end = True
        
