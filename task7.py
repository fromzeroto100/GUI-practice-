from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", 
          "cyan", "magenta", "pink", "purple", "teal", "lime", "brown", "gray"]

walks = [t.back, t.fd, t.right, t.left]

for walk in walks in range(100):
    t.color(random.choice(colors))
    random.choice(walks)(10)






screen = Screen()
screen.exitonclick()