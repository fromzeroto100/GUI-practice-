from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.pensize(16)
t.speed(speed=0)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", 
          "cyan", "magenta", "pink", "purple", "teal", "lime", "brown", "gray"]

# walks = [t.back, t.fd, t.right, t.left]

# for walk in walks in range(100):
#     t.color(random.choice(colors))
#     random.choice(walks)(10)
directions = [0, 90, 180, 270]

for _ in range(100):
    t.fd(35)
    t.setheading(random.choice(directions))
    t.color(random.choice(colors))


screen = Screen()
screen.exitonclick()