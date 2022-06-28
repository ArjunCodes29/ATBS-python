import random

guess = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
print('')

for guessCount in range(1,7):
    print('Take a guess.')
    userGuess = int(input())

    if userGuess == guess:
        break
    elif userGuess > guess:
        print('Your guess is too high.')
    else:
        print('Your guess is too low.')

if guess==userGuess:
    if guessCount > 1:
        print('Good job! you guessed my number in ' + str(guessCount) + ' guesses')
    else:
        print('Wow! Amazing job! you guessed my number in' + str(guessCount) + 'guess')
else:
    print('Nope the number I was guessed was ' + str(guess) + '')
    