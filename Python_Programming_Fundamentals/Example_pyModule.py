#
# Creating and using Custom Modules
#
# Project structure looks like this...
#    my_project/
#          main.py
#          geometry_calculations.py


#------- MODULR FILE -------#
# The module file holds the functions and classes.
# File: geometry_calculations.py
#
import math

def calculate_area_circle(radius):
    """Calculates the area of a circle given its radius."""
    return math.pi * radius**2

def calculate_circumference_circle(radius):
    """Calculates the circumference of a circle given its radius."""
    return 2 * math.pi * radius

class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def calculate_perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)



#------- MAIN FILE -------#
# MAIN module calls import to access your module file. 
# File: main.py
#
import geometry_calculations

radius = 5
area = geometry_calculations.calculate_area_circle(radius)
circumference = geometry_calculations.calculate_circumference_circle(radius)

print(f"Area of circle: {area}")
print(f"Circumference of circle: {circumference}")

rect = geometry_calculations.Rectangle(4, 6)
rect_area = rect.calculate_area()
rect_perimeter = rect.calculate_perimeter()

print(f"Area of rectangle: {rect_area}")
print(f"Perimeter of rectangle: {rect_perimeter}")
