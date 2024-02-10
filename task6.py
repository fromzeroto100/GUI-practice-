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

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        my_turtle.fd(100)
        my_turtle.right(angle)


for shape_side_n in range(3, 11):
    my_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)
















screen = Screen()
screen.exitonclick()