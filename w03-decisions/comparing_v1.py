"""
Author: Edi Carlos

Purpose: Practicing if statements
"""

print("Compare two numbers!\n")

first = int(input("Write the first number: "))

second = int(input("Write the second number: "))

if first > second:
    print("\nThe first number is greater.")
else:
    print("\nThe first number is not greater.")

if first == second:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

if second > first:
    print("The second number is greater.\n")
else:
    print("The second number is not greater.\n")

print() # blank line!

print("Comparing favorite animals with the programmer")

my_favorite_animal = "dog"

user_favorite_animal = input("What is your favorite animal? ")
user_favorite_animal = user_favorite_animal.lower()

if user_favorite_animal == my_favorite_animal:
    print("That's my favorite animal too!\n")
else:
    print("That one is not my favorite.\n")

