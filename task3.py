from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("green")

for _ in range (10):
    t.fd(10)
    t.penup()
    t.fd(10)
    t.pendown()



screen = Screen()
screen.exitonclick()