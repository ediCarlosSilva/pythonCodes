"""
Program: compute the areas 
Author: Edi Carlos

Description: A program to compute the areas of three different shapes: a square, a rectangle, and a circle.
"""
import math

length = float(input("What is the length of a side of the square? "))
area = length ** 2
print(f"The area of the square is: {area:.1f}\n")

length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
area = length * width
print(f"The area of the rectangle is: {area:.1f}\n")

radius = float(input("What is the radius of the circle? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.1f}\n")

