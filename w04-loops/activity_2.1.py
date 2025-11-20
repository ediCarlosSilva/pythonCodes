"""
Author: Edi Carlos
Purpose: Practice using for loops.

Activity 1: Given the following list of items.
Use a for loop to iterate through this list one by one and display each item on its own line as follows

Activity 2: Use a for loop to display the numbers 1–8, one number on each line as follows:

activity 3: Use a for loop to display the even numbers (hint: count by two) 2–20, one number on each line as follows:
"""

print("Activity 1\n")

colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(color)

print("\nActivity 2\n")

for i in range(1, 9, 1):
    print(i)

print("\nActivity 3\n")

for i in range(2, 21, 2):
    print(i)