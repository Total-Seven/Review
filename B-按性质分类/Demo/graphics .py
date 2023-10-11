from turtle import *
import colorsys


def initial():
    setup(1900, 1000, 0, 0)
    screensize(1800, 900)
    goto(0, -50)
    speed()
    hideturtle()
    bgcolor('black')
    tracer(5)
    width(2)


initial()
h = 0.001
for i in range(90):
    color(colorsys.hsv_to_rgb(h, 1, 1))
    forward(100)  # 向前
    left(60)  # 向左
    forward(100)  # 再向前
    left(120)  # 向右

    circle(50)

    left(240)  # 向左
    forward(100)  # 向前
    left(60)  # 再向左
    forward(100)  # 再向前

    h += 0.02

    color(colorsys.hsv_to_rgb(h, 1, 1))
    forward(100)
    right(60)
    forward(100)
    left(120)

    circle(-50)

    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)

    h += 0.02

done()
