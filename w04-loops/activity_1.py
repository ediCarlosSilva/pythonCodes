"""
Author: Edi Carlo
Program: Activiy about loop

Activity: Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number. For example:
"""

number = -1
while(number <= 0):
    number = float(input("Please type a positive number: "))

    if number < 0:
        print("Sorry, that is a negative number. Please try again.")

print(f"The number is: {number:.2f}")
