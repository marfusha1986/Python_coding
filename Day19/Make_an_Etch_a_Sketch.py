from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_on():
    tim.forward(18)

def backwards():
    tim.backward(10)

def turn_left():
    new_tim_heading = tim.heading() + 10
    tim.setheading(new_tim_heading)

def right():
    new_tim_heading = tim.heading() - 10
    tim.setheading(new_tim_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_on,"w")
screen.onkey(backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(right,"d")
screen.onkey(clear,"c")
screen.exitonclick()


#W=Forwards
#S=Backwards
#A=Counter-Clockwise
#D=Clockwise
#C=Clear..
