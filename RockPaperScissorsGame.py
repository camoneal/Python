import random, sys

print('Rock, Paper, Scissors')

#These variables keep track of the number of wins, losses, and ties.
wins=0
losses=0
ties=0

while True: #The main loop of the game
    print('%s Wins, %s Losses, %s ties' % (wins, losses, ties))
    while True: # Players input to the loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quits the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop
        print('Type one of r,p,s, or q.')

    #Displays what the player choose:
    if playerMove == 'r':
        print('Rock versus ...')
    elif playerMove == 'p':
        print('Paper versus ...')
    elif playerMove == 's':
        print('Scissors versus ...')

    #displays what the computer chooses
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove ='r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove ='p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove ='s'
        print('SCISSORS')

#Displays and records the win/loss/tie:
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties +1 
    elif playerMove =='r' and computerMove == 's':
        print('You Win') 
        wins = wins +1
    elif playerMove == 'p' and computerMove =='r':
        print('You Win') 
        wins = wins +1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win') 
        wins = wins + 1
    elif playerMove ==  'r' and computerMove == 'p':
        print('You Lose!') 
        losses = losses +1
    elif playerMove == 'p' and computerMove =='s':
        print('You Lose!') 
        losses=losses +1
    elif playerMove == 's' and computerMove =='r':
        print('You Lose!') 
        losses=losses +1


