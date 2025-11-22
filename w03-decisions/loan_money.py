"""
Author: Edi Carlos
Program: Qualifying for a loan Program

Description: A program to determine whether to loan money based on the following rules.
"""

print("Qualifying for a loan Program!\n")

# First, ask for a rating from 1–10 on the following:
print("Please, enter the rating from 1-10 of the following:\n")

loan_size = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income_high = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

can_loan = False

if loan_size >= 5:
    if credit_history >= 7 and income_high >= 7:
        can_loan = True
    elif credit_history >=7 or income_high >= 7:
        if down_payment >= 5:
            can_loan = True
        else:
            can_loan = False
    else:
        can_loan = False
else: # This means its a small loan       
    if credit_history < 4:
        can_loan = False
    else:
        if income_high >= 7 or down_payment >= 7:
            can_loan = True
        elif income_high >= 4 and down_payment >= 4:
            can_loan = True
        else:
            can_loan = False

if can_loan:
    print("Conglatulations! You can get the loan!")
else:
    print("Sorry! At the moment you cannot take the loan!")