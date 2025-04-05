import math
def calculate_circumfernce(radius):
    cirmunfernce = 2 * math.pi * radius
    return cirmunfernce
radius = float(input("enter a radius:"))
print("the circumfrence of the circle woth radius {radius} is {calculate_circumfernce}")