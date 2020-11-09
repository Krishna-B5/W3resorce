# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
from math import pi

radius = float(input("Enter the radius of the circle : "))
# print(type(radius))

area = pi * radius ** 2 
print("Area of the circle {0}".format(area))