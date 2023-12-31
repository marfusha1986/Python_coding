from turtle import Screen,Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for pos in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments) - 1,0,-1):#start,stop,step
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)



screen.exitonclick()