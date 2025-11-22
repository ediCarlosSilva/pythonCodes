"""
Author: Edi Carlos
Purpose: Activity week 4
"""
word = "Jesus is my Savior."

favorite_letter = input("What is your favorite letter? ")

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
