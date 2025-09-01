
#*************** GUESS THE NUMBER - Mini Project *****************#

# We will generate a random number between 1 and 100 using python and then we will ask the user to guess the number by giving input to the console.
# Then, If the guessed number is less than the randomly generated number than the user will be prompted to guess a higher number.
# If the guessed number is greater than the randomly generated number than the user will be prompted to guess a lower number.
# If the guessed number is equal to the randomly generated number then the user will be congratulated.

import random

target = random.randint(1, 100)

while True:
    userInput = input("Guess the Number or Quit the game by pressing 'Q': ")
    if userInput.lower() == 'q':
        print("You Quit the game.")
        break

    userChoice = int(userInput)
    if(userChoice < target):
        print("Guess a Higher Number")
    elif(userChoice > target):
        print("Guess a Lower Number")
    else:
        print("Congratulations! You guessed the number.")
        break

print("Game Over!!")
