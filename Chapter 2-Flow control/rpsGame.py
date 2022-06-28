# This game simulates Rock paper sccisors with a robot

import sys, random

print('ROCK, PAPER SCISSORS')
winCount= 0
lossCount= 0
tieCount= 0

while True:
    print(str(winCount) + ' Wins, ' + str(lossCount) + ' Losses, ' + str(tieCount) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    inta= str(input())
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'Rock'
    elif randomNumber == 2:
        computerMove = 'Paper'
    else:
        computerMove = 'Sciccsors'

    if inta=='q':
        sys.exit()
    elif inta=='p':
        print('PAPER VERSUS...')
        print('')
        print(computerMove)
        if randomNumber == 1:
            print('You win!')
            winCount += 1
        elif randomNumber == 2:
            print('It is a tie!')
            tieCount += 1
        else:
            print('You lose :(')
            lossCount+= 1
    elif inta=='r':
        print('ROCK VERSUS...')
        print('')
        print(computerMove)
        if randomNumber == 3:
            print('You win!')
            winCount += 1
        elif randomNumber == 1:
            print('It is a tie!')
            tieCount += 1
        else:
            print('You lose :(')
            lossCount+= 1
    elif inta=='s':
        print('SCISSORS VERSUS...')
        print('')
        print(computerMove)
        if randomNumber == 2:
            print('You win!')
            winCount += 1
        elif randomNumber == 3:
            print('It is a tie!')
            tieCount += 1
        else:
            print('You lose :(')
            lossCount+= 1
    else:
        print('Try again')