# import turtle
import turtle

# input
num_sides = int(input("Enter the number of sides of the polygons you would like to use for your pattern: "))

# constant
total_shapes = 20

# variables
interior_angle = (360 / num_sides)
angle_between_shapes = (360 / total_shapes)

# for-loop
for iteration in range(total_shapes):
    # for-loop
    for side in range(num_sides):
        turtle.forward(50)
        turtle.left(interior_angle)
        turtle.forward(50)
      
    # adjust turtle position to turn to draw another shape
    turtle.left(angle_between_shapes) 
