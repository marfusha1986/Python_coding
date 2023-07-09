from turtle import Turtle,Screen
import random
tom = Turtle()
tom.shape("turtle")

colors = ["Honeydew","Goldenrod","SaddleBrown","YellowGreen","Salmon","Chartreuse","LightCoral","DarkOliveGreen","DarkSeaGreen","NavajoWhite"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tom.forward(100)
        tom.right(angle)
for shape_side_n in range(3, 11):
    tom.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()