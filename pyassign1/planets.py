#!/usr/bin/env python3
"""Planets.py: Description of how planets in solar system move.
__author__ = "Liu Yuxin"
__pkuid__  = "1800011832"
__email__  = "1800011832@pku.edu.cn"
"""

import turtle
wn=turtle.Screen()
turtle.screensize(800,600)
wn.delay(0)

sun=turtle.Turtle()
sun.color("orange")
sun.dot(7)
sun.hideturtle()

def initialization(t,r,a,c,colors):#t standing for planets,r standing for radius,a standing for major semiaxis,c standing for excentricity
    t.shape("circle")
    t.shapesize(r,r,r)
    t.color(colors)
    t.pencolor(colors)
    t.penup()
    t.speed(0)
    t.setx(a+c)
    t.pd()

def orbits(t,a,c,i,x):
    t.speed(0)
    import math
    t.goto(a*(math.cos((math.pi)*(i+1)/x))+c,math.sqrt(a**2-c**2)*math.sin((math.pi)*(i+1)/x))
def main():
    Mercury=turtle.Turtle()
    Venus=turtle.Turtle()
    Earth=turtle.Turtle()
    Mars=turtle.Turtle()
    Jupiter=turtle.Turtle()
    Saturn=turtle.Turtle()

    initialization(Mercury,0.1,8.7,4.2,"blue")
    initialization(Venus,0.2,16.2,0.26,"green")
    initialization(Earth,0.21,22.5,0.875,"brown")
    initialization(Mars,0.15,34.2,7.455,"red")
    initialization(Jupiter,0.358,116,13.3,"sea green")
    initialization(Saturn,0.303,200,28,"yellow")

    while True:
        for i in range(960):
            orbits(Mercury,8.7,4.2,i,60)
            orbits(Venus,16.2,0.26,i,96)
            orbits(Earth,22.5,0.875,i,120)
            orbits(Mars,34.2,7.455,i,160)
            orbits(Jupiter,116,13.3,i,240)
            orbits(Saturn,200,28,i,480)
if _name_=="_main_":
    main()