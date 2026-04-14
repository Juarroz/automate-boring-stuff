import random, sys

print('Rock Paper Scissors.')

# These variables keep track of the number of wins, losses and ties
wins = 0
loses = 0
ties = 0

while True:

    print(f'{wins} wins, {loses} Losses, {ties} ties')

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit.')
        player_move = input('> ').lower()

        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p'or player_move == 's':
            break
        print('Invalid input. Try again.')

    # Display what the player chose:
    if player_move == 'r':
        print('Rock versus...')
    if player_move == 'p':
        print('Paper versus...')
    if player_move == 's':
        print('Scissors versus...')

    # Display what the computer chose
    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('Rock')
    if move_number == 2:
        computer_move = 'p'
        print('Paper')
    if move_number == 3:
        computer_move = 's'
        print('Scissors')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        loses += 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        loses += 1
    elif player_move == 'p' and computer_move == 's':
        print('You win!')
        loses += 1
