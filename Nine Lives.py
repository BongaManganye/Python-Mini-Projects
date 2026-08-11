#Nine Lives
# In this nerve-shredding game, you have to guess the secret word one letter at a time
# If your guess is wrong, you  lose a life. Choose your letters carefully, because you only have nines lives.
# Lose all your, and it's game over

#How it works
# First you'll create two lists: one to stone the secret words and one to store the clue,
# Which is made up of question marks. Then, using the random module, you'll make a random selection from the list of secret words.
# Next you'll build a loop to check the player's guesses, and also create a function to update the clue as the word is slowly revealed.

import random

lives = 9 #The player starts with nine lives
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane'] #Each item in the list is a string made up of fives characters
secret_word = random.choice(words) # This variable uses the random module's choice() function.
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1 #Add 1 to the index value

while lives > 0: #The loop keeps running while there are lives left
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ') #This gets the guessed letter or the player

    if guess == secret_word:
        guessed_word_correctly = True
        break #When the word is guessed correctly, this line breaks the loop.

    if guess in secret_word: #If the guessed letter is in the secret word, the clue is updated
        update_clue(guess, secret_word, clue)
    else: #If the guess is incorrect (else), the number of lives is reduced by 1
        print('Incorrect. You lose a life') 
        lives = lives - 1
if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)
