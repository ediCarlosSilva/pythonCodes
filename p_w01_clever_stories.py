# Additional creativity: Added a title before the sentence accordly to the field [animal]. If the word begins with a vowel the title will begin with letter An, otherwise it will begin with letter A.

"""
Program: Clever Stories
Author: Edi Carlos

Description: A program for Clever Stories like Mad Libs. Mad Libs are a type of funny story, where a person is asked for words without knowing their context. The words are then placed into a story in a pre-determined format, often resulting in funny statements.
"""

print("------------------------------------------------------------------\n")
print("Clever Stories Program!\n")

print("Please enter the following:")

adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")

# Variable additional creativity
firstVowel = ""

print("\nYour story is: \n")

# The logic for the title
firstVowel = animal[0]

if firstVowel in ['a', 'e', 'i', 'o', 'u']:
    print(f"An {animal.title()} Story!\n")
else: 
    print(f"A {animal.title()} Story!\n")
# End of the logic for the title

print(f"The other day, I was really in trouble. It all started when I saw a very {adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all I could think to do was to {verb2.lower()} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3.lower()} right in front of my family.")