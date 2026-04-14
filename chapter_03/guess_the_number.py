# this is a guess the number game

import random

secret_number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

# ask the player to guess 6 times
for guesses in range(1, 7):
    guess = int(input('Guess the number between 1 and 100: '))

    if guess < secret_number:
        print(f'Your guess is too low.')
    elif guess > secret_number:
        print(f'Your guess is too high.')
    else:
        break

if guess == secret_number:
    print(f'Good job, you guessed the number {guess}.')
    print(f'You guessed the number {secret_number} in {guesses} guesses.')
else:
    print(f'Nope. The number I was thinking of was {secret_number}.')







