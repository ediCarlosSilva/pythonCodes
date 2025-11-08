"""
Program: ID Badge Generator
Author: Edi Carlos

Description: a program that will create a properly formatted ID badge.
"""

print("ID Badge Generator\n")

print("Please enter the following information:")

first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

print("\nThe ID Card is:\n")
print("----------------------------------------")
print(f"{last_name.upper()}, {first_name}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone_number)
print("----------------------------------------")