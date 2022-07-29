from svg_turtle import *

def square(alex: SvgTurtle, side: int):
    x, y = alex.pos()
    alex.goto(x, y + side)
    alex.goto(x + side, y + side)
    alex.goto(x + side, y)
    alex.goto(x, y)

tim = SvgTurtle()
tim.color('cyan')

square(tim, 10)
tim.fd(100)
square(tim, 30)
tim.goto(20, 32)
square(tim, 50)
square(tim, 27)

tim.save_as('image.svg')