# With this example, you have access to both the letter and the index at each step of the loop.

word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")