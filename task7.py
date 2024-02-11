from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.pensize(16)
t.speed(speed=0)
t.colormode(255)
# walks = [t.back, t.fd, t.right, t.left]

# for walk in walks in range(100):
#     t.color(random.choice(colors))
#     random.choice(walks)(10)
directions = [0, 90, 180, 270]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(100):
    t.fd(35)
    t.setheading(random.choice(directions))
    t.color(random_color())


screen = Screen()
screen.exitonclick()