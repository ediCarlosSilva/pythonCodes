"""
Program: Bond, James Bond
Author: Edi Carlos

Description: Display the name in a sequence like Bond, James Bond
"""

# gather first and last name
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# first activity
print(f"Your name is {last_name}, {first_name} {last_name}.")

# This is for the the second part, where we adjust the capitalization
print(f"Your name is {last_name.title()}, {first_name.title()} {last_name.title()}.")