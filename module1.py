#-------------------------------------------------------------------------------
# Name:        module1 exercise
# Purpose:      practice exercise on function for area and perimeter of a circle
#
# Author:      André Domingues
#
# Created:     26/01/2023
# Copyright:   (c) alodb 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Pi = 3.14
r = int(input("Enter radius of circle: "))

# This line calculates the area of the circle:
circle_area = Pi * r**2
print("The area of the circle is: ", circle_area)


# This line calculates the perimeter of the circle:
circle_perimeter = 2 * Pi * r
print("The perimeter of the circle is: ", circle_perimeter)