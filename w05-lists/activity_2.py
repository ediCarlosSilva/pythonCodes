"""
Author: Edi Carlos
Purpose: Practice using lists and list indexes.
"""

shoppings_list = []
item = None

print("Please enter the items of the shopping list (type: quit to finish):")

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        shoppings_list.append(item)

print()    
print("The shopping list is:")
for item in shoppings_list:
    print(item.capitalize())

print()
print("The shopping list with indexes is:")
for i in range(len(shoppings_list)):
    item = shoppings_list[i]
    print(f"{i}. {item.capitalize()}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shoppings_list[index] = new_item

print()
print("The shopping list with indexes is:")
for i in range(len(shoppings_list)):
    item = shoppings_list[i]
    print(f"{i}. {item.capitalize()}")