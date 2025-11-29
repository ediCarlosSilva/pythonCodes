# added list of quantities to the cart in line 11. Logic for that in each option of the cart (lines 34 - 35, lines 40 - 46, line 64, and line 70)
"""
Author: Edi Carlos
Program: shopping Cart

Description: A program that stores a list of products in a shopping cart along with their prices.
"""

list_of_names = []
list_of_prices = []
list_of_quantities = []

option = ""

print("Welcome to the Shopping Cart Program!")

while option != "5":
    print("""\nPlease select one of the following: 
            1. Add item
            2. View cart
            3. Remove item
            4. Compute total
            5. Quit
    """)
    option = input("Please enter an action: ")

    if option == "1":
        item_name = input("What item would you like to add? ")
        list_of_names.append(item_name)

        item_price = float(input(f"What is the price of '{item_name}'? "))
        list_of_prices.append(item_price)

        item_quantity = int(input(f"What is the quantity of '{item_name}'? "))
        list_of_quantities.append(item_quantity)

        print(f"'{item_name}' has been added to the cart.")
    elif option == '2':
        print("The contents of the shopping cart are:")
        total_amount = 0
        for i in range(len(list_of_names)):
            amount = list_of_prices[i] * list_of_quantities[i]
            total_amount += amount
            print(f"{i + 1}. {list_of_names[i]} - ${list_of_prices[i]:.2f} - quantity: {list_of_quantities[i]} - amount: {amount:.2f}")
        
        print(f"\nThe total price of the items in the shopping cart is {total_amount}")
    elif option == '3':
        print("The contents of the shopping cart are:")
        for i in range(len(list_of_names)):
            print(f"{i + 1}. {list_of_names[i]} - ${list_of_prices[i]:.2f}")

        print()
        item_to_remove = -1
        while item_to_remove < len(list_of_names):
            item_to_remove = int(input("\nWhich item would you like to remove? (hit 0 to return to menu) "))
            if item_to_remove == 0:
                break
            elif item_to_remove > len(list_of_names):
                item_to_remove = -1
                print("Sorry, that is not a valid item number.")
            else:
                list_of_names.pop(item_to_remove - 1)
                list_of_prices.pop(item_to_remove - 1)
                list_of_quantities.pop(item_to_remove - 1)
                print("Item removed.")
    elif option == '4':
        amount = 0
        for i in range(len(list_of_prices)):
            amount += (list_of_prices[i] * list_of_quantities[i])
        print(f"The total price of the items in the shopping cart is ${amount}")
    elif option == '5':
        break
    else:
        print("\nInvalid option!!!\n")
    
print("Thank you. Goodbye.")
