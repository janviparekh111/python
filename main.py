// write a python program to calculate the area and circumference of a circle by accepting the radius from the user

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print("Area of circle =", area)
print("Circumference of circle =", circumference)