
# # Guess the number

# This notebook simulates a classic game
# where you have to guess a random number from within a certain range.
# Typically, you might have to guess a number from 1 to 10,
# and have three guesses to get the right answer.

# In this case, you'll need to guess a random number between 1 and 100,
# and you will have 7 tries.

# Try running it and playing a round or two.
# Notice that the game always tells you whether your guess was too high or too low.
# This information allows you to rule out
# some of the numbers (so that you don't waste time guessing those numbers).

# With this fact in mind,
# try to make your guesses in the most efficient way you can.
# Specifically, try to make guesses that rule out the largest number
# of possibilities each time.


import random

def guess_the_number(total_tries, start, end):
    random_number = random.randint(start, end)
    num_tries = 0
    s_message = "Awsome! You guessed the number in {} tries."
    f_message = "sorry you didn't guess the number in {} tries."
    miss_missage = 'Sorry, that was not the number I was thinking of.'
    
    while total_tries > num_tries:
        guess = int(input('Guess a number between {} and {}: '.format(start, end)))
        if guess == random_number:
            print(s_message.format(num_tries + 1))
            return
        elif guess > random_number:
            print('Your guess was too high.')
        else:
            print('Your guess was too low.')
        num_tries += 1
    print("the number was {}".format(random_number))
guess_the_number(7, 1, 100)