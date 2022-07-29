from svg_turtle import *

tim = SvgTurtle()
tim.color('white')
tim.circle(50)
tim.fd(50)
tim.circle(70)
tim.goto(100, 100)
tim.circle(25)

tim.save_as('image.svg')