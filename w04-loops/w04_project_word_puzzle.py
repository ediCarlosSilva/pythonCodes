# Showing Creativity: I used random library to get the secret word from a list. You can see the code from line 8 to 12
"""
Author: Edi Carlos
Program: Word Puzzle

Description: An interactive word puzzle game that allows the user to make guesses until they get the answer correct, and hints are provided along the way.
"""
import random

list_of_word = ["jesus", "mosiah", "moroni", "alma", "jacob", "helaman", "nephi", "lehi", "mormon", "enos", "omni", "ether"]
random_index = random.randint(1, len(list_of_word) - 1)
secret_word = list_of_word[random_index]

number_letter_of_secret_word = len(secret_word)

print("Welcome to the word guessing game!")

print("\nWhile gaming, you can hit the keys: ctrl + c (at any time), to end the game.\n")

guessed_word = ""
guesses = 0
hint = ""

for index in range(number_letter_of_secret_word):
            hint += "_"

while guessed_word != secret_word:        

    print("Your hint is: ", end="")
    
    print(*hint, sep=" ")
    hint = ""
          
    guessed_word = input("\nWhat is your guess? ")
    guessed_word = guessed_word.lower()

    number_letter_of_guessed_word = len(guessed_word)

    while number_letter_of_guessed_word != number_letter_of_secret_word:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        guesses += 1

        guessed_word = input("\nWhat is your guess? ")
        guessed_word = guessed_word.lower()

        number_letter_of_guessed_word = len(guessed_word)
     
    for index in range(number_letter_of_guessed_word):
        if guessed_word[index] == secret_word[index]:
            hint += guessed_word[index].upper()
        else:
            hint += "_"

    array_hint = list(hint)
    for index in range(number_letter_of_guessed_word):
         if guessed_word[index] in secret_word:
              if guessed_word[index] != secret_word[index]:
                   array_hint[index] = guessed_word[index]

    hint = "".join(array_hint)

            # else:
            #     hint += guessed_word[index].lower()

    guesses += 1

print("Congratulations! You guessed it!")    
print(f"It took you {guesses} guesses.")

