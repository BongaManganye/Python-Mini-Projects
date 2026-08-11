# Animal Quiz
# The program asks the player some questions about animals.
# They get three chances to answer each question you don't 
# want to make the quiz too difficult! Each correct answer will
# Score one point. At the end of the quiz, the program reveals
# the player's final score

def check_guess(guess, answer): #Gives the function a name and parameters
    global score #score variable is global variable, It ensure that changes to the variable can be seen throughout the whole program
    if guess.lower() == answer.lower():
        print('Correct answer')
        score = score + 1 #Add 1 to the player's score
score = 0

print('Guess the Animal!')
guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'polar bear') #Tells the fuction to use the player's guess as the first parameter and the second phrase as the secomd parameter
guess2 = input('Which is the fastest land animal?')
check_guess(guess2, 'cheetah')
guess3 = input('Which is the largest animal')
check_guess(guess3, 'blue whale')

print('Your score is ' + str(score))
