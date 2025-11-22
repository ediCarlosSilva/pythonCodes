"""
Author: Edi Carlos
Purpose: A game where the computer selects a random number and the user tries to guess it
"""
import random
# print(number)

guesses = 1

want_play = "yes"

while want_play == "yes":
    random_number = random.randint(1, 100)
    guess_number = int(input("What is your guess? "))
    while guess_number != random_number:
        if guess_number < random_number:
            print("Lower")
            guesses += 1
        else:
            print("Higher")
            guesses += 1
        
        guess_number = int(input("What is your guess? "))

    print("You guessed it!")
    print(f"It took you {guesses} guesses")

    want_play = input("Would you like to play again (yes/no)? ")
    want_play = want_play.lower()

print("Thank you for playing. Goodbye.")





