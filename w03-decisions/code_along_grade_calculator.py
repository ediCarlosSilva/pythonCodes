"""
Author: Edi Carlos
Program: Grade Calculator Program

Description: A program that determines the letter grade for a course according to scale
"""

scale = int(input("What is the scale of your course. Hit a number from 0 to 100: "))
letter_grade = str()

if scale >= 90:
    if scale < 93:
        letter_grade = 'A-'
    else:
        letter_grade = 'A'
elif scale >= 80:
    if scale >= 87:
        letter_grade = 'B+'
    elif scale < 83:
        letter_grade = 'B-'
    else:
        letter_grade = 'B'
elif scale >= 70:
    if scale >= 77:
        letter_grade = 'C+'
    elif scale < 73:
        letter_grade = 'C-'
    else:
        letter_grade = 'C'
elif scale >= 60:
    if scale >= 67:
        letter_grade = 'D+'
    elif scale < 63:
        letter_grade = 'D-'
    else:
        letter_grade = 'D'
else:
    letter_grade = 'F'

if scale >= 70:
    print(f"Congratulation! You passed! Your grade letter is: {letter_grade}, and your scale is: {scale}%.")
else:
    print("Sorry! Try to study more.")