# from line 25 to 59 there is the code to add extras (drink, appertizes, and tip percentage) to the meal
# in line 73 to 76 there is other code to verify if the payment amount is less than total of the meal
"""
Program: Meal Price Calculator
Author: Edi Carlos

Description: A program to calculate the price of a meal.
"""
import locale

# code for currency location
currency_symbol = '$'
locale_value = 'en_US.UTF-8'
# Set the locale parameters and convert the value 
locale.setlocale(locale.LC_ALL, locale_value)

# get the inputs and compute the main subtotal
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of a adult's meal? "))
children_quantity = int(input("How many children are there? "))
adults_quantity = int(input("How many adults are there? "))

subtotal_main = (children_quantity * child_price) + (adults_quantity * adult_price)

# extra code, asking for drinks, appetizers, or a tip percentage
extra_quantity = 0
extra_price = 0
extra_percentage = 0
total_drink = 0
total_appetizer = 0
total_tip = 0
subtotal_extras = 0

desire = int(input("Would you like to add a drink? ((hit 1 for yes, any key for not)) "))
if desire == 1:
    extra_quantity = int(input("How many drinks would you like to add? "))
    extra_price = float(input("What is the price of the drink? "))
    total_drink = extra_quantity * extra_price

desire = int(input("Would you like to add a appetizers? ((hit 1 for yes, any key for not)) "))
if desire == 1:
    extra_quantity = int(input("How many appetizers would you like to add? "))
    extra_price = float(input("What is the price of the appetizer? "))
    total_appetizer = extra_quantity * extra_price

desire = int(input("Would you like to add a tip percentage? ((hit 1 for yes, any key for not)) "))
if desire == 1:
    extra_percentage = float(input("What percentage would you like to add?\nEnter the percentage as whole number: "))
    total_tip = (subtotal_main + total_drink + total_appetizer) * (extra_percentage / 100)

if total_drink != 0 or total_appetizer != 0 or total_tip != 0:
    subtotal_extras = (total_drink + total_appetizer + total_tip)

subtotal = subtotal_main + subtotal_extras

# format the subtotal for dollar currency
subtotal_formatted = locale.currency(subtotal, grouping=True, symbol=currency_symbol)

print(f"\nSubtotal: {subtotal_formatted}\n")

# compute tax rate
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * (tax_rate / 100)
sales_tax_formatted = locale.currency(sales_tax, grouping=True, symbol=currency_symbol)
print(f"Sales Tax: {sales_tax_formatted}")

total = subtotal + sales_tax
total_formatted = locale.currency(total, grouping=True, symbol=currency_symbol)

print(f"Total: {total_formatted}\n")

# getting the payment amount
payment_amount = float(input("What is the payment amount? "))
while payment_amount < total:
    print("Sorry, payment amount can not be less than total.")
    payment_amount = float(input("What is the payment amount? "))

# compute the change
change = payment_amount - total
change = locale.currency(change, grouping=True, symbol=currency_symbol)
print(f"Change: {change}")