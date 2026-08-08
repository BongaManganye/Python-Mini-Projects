#Guessing Game
#Generate a random number between 1 and 100. Write a loop allowing the user to 
#guess until correct providing "Too high" or "Too Low" feedback and counting total attempts 

import random

num1 = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Please enter a number between 1 and 100"))
    attempts += 1
    if num1 > guess:
        print("Too high")
    elif num1 < guess:
        print("Too  low")
    else:
        print(f"Correct in {attempts} attempts!")
        break
