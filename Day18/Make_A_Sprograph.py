import turtle as t
import random

tom = t.Turtle()
tom.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tom.speed("fastest")

def draw_spirograph(size_of_gap):
    for shape_side_n in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(5)
screen=t.Screen()
screen.exitonclick()