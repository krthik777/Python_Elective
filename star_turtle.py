import turtle
import math

t = turtle.Turtle()
t.penup()

def draw_star(size):
    offset = math.sin(math.radians(18)) * size
    height = offset / math.cos(math.radians(54))

    t.left(126)
    t.forward(height)
    t.left(54)
    t.forward(size)
    t.right(180)
    t.pendown()

    for _ in range(5):
        t.forward(size)
        t.left(72)
        t.forward(size)
        t.right(144)

    t.penup()
    t.forward(size)
    t.right(54)
    t.forward(height)
    t.left(54)

num_stars = int(input("Enter the number of stars: "))
star_size = int(input("Enter the size of each star: "))
star_color = input("Enter the star color: ")

t.pencolor(star_color)
angle = 360 / num_stars

for _ in range(num_stars):
    t.forward(200)
    t.right(angle)
    draw_star(star_size)
    t.goto(0, 0)
