from svg_turtle import *

tim = SvgTurtle()
tim.dot(10)
tim.goto(10, 10)
tim.dot(15)

tim.save_as('image.svg')