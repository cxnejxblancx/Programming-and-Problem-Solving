"""
Formulas:
    - Volume of a Sphere:
        V = (4 / 3) * pi * (r ** 3)

    - Volume Right Circular Cone:
        V = pi * (r ** 2) * (h / 3)
"""

# input
num_scoops = int(input("Enter the number of ice cream scoops you want: "))
cone_radius = float(input("Enter the radius of ice cream cone: "))
cone_height = float(input("Enter the height of ice cream cone: "))

# calculations
total_scoop_volume = (num_scoops * ((4 / 3) * (3.1416) * (cone_radius ** 3)))
cone_volume = (3.1416) * ((cone_radius) ** 2) * (cone_height / 3)
total_scoop_cone_volume = (total_scoop_volume + cone_volume)

# print
print("Your " + str(num_scoops) + " scoop ice cream cone has a total volume of " + str(total_scoop_cone_volume))
