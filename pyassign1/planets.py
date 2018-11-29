#!/usr/bin/env python3
"""Planets.py: Description of how planets in solar system move.
__author__ = "Liu Yuxin"
__pkuid__  = "1800011832"
__email__  = "1800011832@pku.edu.cn"
"""

import turtle
wn = turtle.Screen()
turtle.screensize(800, 600)
wn.delay(0)


def initialization(t, r, a, c, colors):
    # t standing for planets,r standing for radius,a standing for major semi-axis,c standing for semi focal distance
    t.shape("circle")
    t.shapesize(r, r, r)
    t.color(colors)
    t.pencolor(colors)
    t.penup()
    t.speed(0)
    t.setx(a+c)
    t.pd()


def orbits(t, a, c, i, x):  # i is used in the while loop
    t.speed(0)
    import math
    t.goto(a*(math.cos(math.pi*(i+1)/x))+c, (math.sqrt(a**2-c**2))*math.sin(math.pi*(i+1)/x))


def main():
    sun = turtle.Turtle()
    sun.color("orange")
    sun.dot(7)
    sun.hideturtle()
    mercury = turtle.Turtle()
    venus = turtle.Turtle()
    earth = turtle.Turtle()
    mars = turtle.Turtle()
    jupiter = turtle.Turtle()
    saturn = turtle.Turtle()
    initialization(mercury, 0.1, 8.7, 4.2, "blue")
    initialization(venus, 0.2, 16.2, 0.26, "green")
    initialization(earth, 0.21, 22.5, 0.875, "brown")
    initialization(mars, 0.15, 34.2, 7.455, "red")
    initialization(jupiter, 0.358, 116, 13.3, "sea green")
    initialization(saturn, 0.303, 200, 28, "yellow")
    while True:
        for y in range(960):
            orbits(mercury, 8.7, 4.2, y, 60)
            orbits(venus, 16.2, 0.26, y, 96)
            orbits(earth, 22.5, 0.875, y, 120)
            orbits(mars, 34.2, 7.455, y, 160)
            orbits(jupiter, 116, 13.3, y, 240)
            orbits(saturn, 200, 28, y, 480)


if __name__ == "__main__":
    main()
