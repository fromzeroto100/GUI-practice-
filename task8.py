from turtle import Turtle, Screen
import random

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("green")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", 
          "cyan", "magenta", "pink", "purple", "teal", "lime", "brown", "gray"]

# my_turtle.fd(100)
# my_turtle.right(90)
# my_turtle.fd(100)
# my_turtle.right(90)
# my_turtle.fd(100)
# my_turtle.right(90)
# my_turtle.fd(100)
# my_turtle.right(90)
my_turtle.speed("fastest")


for _ in range(100):
    my_turtle.circle(50)
    my_turtle.color(random.choice(colors))
    my_turtle.setheading(my_turtle.heading() + 10)

















screen = Screen()
screen.exitonclick()