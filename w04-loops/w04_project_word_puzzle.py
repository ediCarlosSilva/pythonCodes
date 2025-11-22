"""
Author: Edi Carlos
Program: Word Puzzle

Description: An interactive word puzzle game that allows the user to make guesses until they get the answer correct, and hints are provided along the way.
"""

secret_word = "mosiah"
number_letter_of_secret_word = len(secret_word)

print("Welcome to the word guessing game!")

print("\nWhile gaming, you can hit the keys: ctrl + c (at any time), to end the game.\n")

guessed_word = ""
guesses = 1
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

    
            # else:
            #     hint += guessed_word[index].lower()

    guesses += 1

print("Congratulations! You guessed it!")    
print(f"It took you {guesses} guesses.")

    
    
    # number_letter_of_guessed_word = len(guessed_word)

    # if number_letter_of_guessed_word != number_letter_of_secret_word:
    #     print("Sorry, the guess must have the same number of letters as the secret word.")
    #     guess += 1

