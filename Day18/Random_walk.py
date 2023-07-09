import turtle as t
import random

tom = t.Turtle()
tom.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


directions = [0, 90, 180, 270]
tom.pensize(20)
tom.speed("fast")

for shape_side_n in range(150):
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))

