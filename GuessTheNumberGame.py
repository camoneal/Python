#This is a guess the number game

import random #module is imported into python
secretNumber= random.randint(0,20) #picks random number between 0 - 20
print('I am thinking of a number between 0 and 20.')

#Ask the player to guess the number 6 times
for guessesTaken in range (1,7): #defines the number of guesses allowed
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess it too high.')
    else:
        break  #This condition is the correct guess

if guess == secretNumber:
    print('Good job! You guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was' + str(secretNumber))
