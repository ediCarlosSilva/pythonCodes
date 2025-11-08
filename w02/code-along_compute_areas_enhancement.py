"""
Program: compute the areas 
Author: Edi Carlos

Description: A program to compute the areas of three different shapes: a square, a rectangle, 
and a circle in centimeters and centimeters square.
"""
import math

side = float(input("What is the length of a side of the square (in centimeters)? "))
area = side ** 2
print(f"The area of the square is: {area:.1f} cm^2")
print(f"The area of the square is: {area / 10000} m^2 (square meters)\n")

length = float(input("What is the length of the rectangle (in centimeters)? "))
width = float(input("What is the width of the rectangle (in centimeters)? "))
area = length * width
print(f"The area of the rectangle is: {area:.1f} cm^2 (in square centimeters)")
print(f"The area of the rectangle is: {area / 10000} m^2 (square meters)\n")

radius = float(input("What is the radius of the circle (in cm)? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.1f} cm^2 (in square centimeters)\n")
print(f"The area of the circle is: {area / 10000} m^2 (in square meters)\n")

