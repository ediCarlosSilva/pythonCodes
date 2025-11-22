"""
Author: Edi Carlos

Purpose: Practicing if statements
"""

print("Comparing favorite animals with the programmer")

my_favorite_animal = "dog"

user_favorite_animal = input("What is your favorite animal? ")
user_favorite_animal = user_favorite_animal.lower()

if user_favorite_animal == my_favorite_animal:
    print("That's my favorite animal too!\n")
else:
    print("That one is not my favorite animal!\n")

