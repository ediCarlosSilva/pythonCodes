"""
Program: Numeric Variables computing
Author: Edi Carlos

Description: Practice using mathematical expression
"""

age = int(input("How old are you? "))
print(f"On you next birthday, you will be {age + 1}\n")

eggs_quantity = int(input("How many egg cartons do you have? "))
print(f"You have {eggs_quantity * 12} eggs\n")

cookies_quantity = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
cookies_per_person = cookies_quantity / people
print(f"Each person may have {cookies_per_person} cookies")