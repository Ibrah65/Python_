#program to compute the surface area of a given cylinder

radius = float(input("Enter the radius of the base of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = 2*(3.14*radius*radius) + 2*(3.14*radius*height)

print("The surface area of the cylinder is:",surface_area)
