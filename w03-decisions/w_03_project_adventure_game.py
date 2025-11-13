"""
Author: Edi Carlos
Program: Adventure Game

Description: A text-based adventure game
"""

print("text-based adventure game!\n".upper())

choice = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")
choice = choice.lower()

if choice == "match":
    choice = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?")
    choice = choice.lower()
elif choice == 'flashlight':
    choice = input("Sequence with flashlight")
    choice = choice.lower()
else:
    print("I don't understande this option, play again.")
