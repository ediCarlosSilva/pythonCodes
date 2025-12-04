"""
Author: Edi Carlos
Purpose: Train open file in python
"""

with open("books.txt") as book_file:

    for line in book_file:

        book = line.strip()
        print(book)