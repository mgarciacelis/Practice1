#1 Area of a Circle
radius = float(input("Radius: "))
from math import pi 
area = round(pi * radius**2, 4)
def circ_area(r):
    return round(pi * r**2, 4)
print("Area: " + str(area))
area = circ_area(radius)

#2 Expression Solver
