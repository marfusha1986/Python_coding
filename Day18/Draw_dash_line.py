from turtle import Turtle,Screen

tom = Turtle()
tom.shape("turtle")
for n in range(30):
    tom.pendown()
    tom.forward(10)
    tom.penup()
    tom.forward(10)
screen = Screen()
screen.exitonclick()