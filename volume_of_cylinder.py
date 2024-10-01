from math import pi, pow

def volume_of_cylinder(radius, height):
    volume = pi * pow(radius, 2) * height 
    return volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = volume_of_cylinder(radius, height)
print(f"The volume of the cylinder is: {volume:.2f}") 
