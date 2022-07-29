from svg_turtle import *


def circles(alex: SvgTurtle):
    alex = SvgTurtle()
    alex.color('white')
    alex.circle(50)
    alex.fd(50)
    alex.circle(70)
    alex.goto(100, 100)
    alex.circle(25)

    alex.save_as('image.svg')