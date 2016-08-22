print('Press enter to play rock paper scissors.')
input('... ')


rps_dict = {'rock':1, 'paper':2, 'scissors':5}

again = 'y'
while again == 'y':
    player1 = str(input('\nPlayer 1, choose rock, paper, or scissors: '))
    player2 = str(input('Player 2, choose rock, paper, or scissors: '))

    choice1 = rps_dict.get(player1)
    choice2 = rps_dict.get(player2)
    total = choice1 - choice2

    if total in [0]:
        print('It is a tie. No one wins.\n')
    elif abs(total) == 1:
        print('Paper covers rock.')
        if total > 0:
            print('Player 1 wins.\n')
        else:
            print('Player 2 wins.\n')
    elif abs(total) == 3:
        print('Scissors cuts paper.')
        if total > 0:
            print('Player 1 wins.\n')
        else:
            print('Player 2 wins.\n')
    elif abs(total) == 4:
        print('Rock breaks scissors.')
        if total > 0:
            print('Player 2 wins.\n')
        else:
            print('Player 1 wins.\n')
    again = str(input('Play again (y/n)? '))
