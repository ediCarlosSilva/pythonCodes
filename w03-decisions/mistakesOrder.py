rewards = 0
choice = "drink"
total_oder = 3

if (choice == "drink" or choice == "cookie") and total_oder > 5:
    rewards += 5

print(f"You have {rewards} rewards points.")