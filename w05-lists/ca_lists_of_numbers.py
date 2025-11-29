"""
Author: Edi Carlos
Program: Lists of Numbers

Description: Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.
"""

numbers = []
user_number = -1

print("Enter a list of numbers, type 0 when finished.")
while user_number != 0:
    user_number = int(input("Enter number: "))
    if user_number != 0:
        numbers.append(user_number)

# using the sum function
# total_sum = sum(numbers)
total_sum = 0
for number in numbers:
    total_sum += number

# average
# average = total_sum / len(numbers)
count = len(numbers)
average = total_sum / count

# the largest
# largest = max(numbers)
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

# the smallest
smallest_positivie = numbers[0]
for number in numbers:
    if number < smallest_positivie and number > 0:
        smallest_positivie = number

# print the results
print(f"The sum is: {total_sum}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
