"""
Program: convert from Fahrenheit to Celsius
Author: Edi Carlos

Description: A program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.
"""

fahrenheit = float(input("What is the temperature in Fahrenheit? "))
degrees = (fahrenheit - 32) * 5 / 9

print(f"The temperature in Celsius is {degrees:.1f} degrees.\n")0