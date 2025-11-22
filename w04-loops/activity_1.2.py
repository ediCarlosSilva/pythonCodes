"""
Author: Edi Carlo
Program: Activiy about loop

Activity: Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you." 
"""

answer = "no"

while answer != "yes":
    answer = input("May I have a piece of candy? ")
    answer = answer.lower()

print("Thank you.")