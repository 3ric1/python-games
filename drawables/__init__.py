import time
import turtle

from turtle import *
from typing import Tuple, Callable, List

class Drawable:
    def __init__(self, pos: Tuple[int, int]):
        self.x, self.y = pos

        self.alex = Turtle(shape='turtle')
        self.alex.speed(0)
        self.alex.hideturtle()

    def move(self, pos: Tuple[int, int]):
        self.x, self.y = pos

    def draw(self):
        pass

    def clear(self):
        self.alex.clear()


class Square(Drawable):
    def __init__(self, pos: Tuple[int, int], side: int, angle: float):
        # self.x, self.y = pos
        # self.alex = Turtle(shape='turtle')
        # self.alex.speed(0)
        # self.alex.hideturtle()
        super().__init__(pos)
        self.side = side
        self.angle = angle

    def draw(self):
        # ajungem la acea pozitie, dar ridicam stiloul prima data
        self.alex.penup()
        self.alex.goto(self.x, self.y)
        # desenam cele 4 linii
        self.alex.pendown()
        self.alex.goto(self.x, self.y + self.side)
        self.alex.goto(self.x + self.side, self.y + self.side)
        self.alex.goto(self.x + self.side, self.y)
        self.alex.goto(self.x, self.y)
        self.alex.penup()

    def movex(self, x):
        self.x = x


class Rectangle(Drawable):
    def __init__(self, pos: Tuple[int, int], width: int, height: int, angle: float):
        # self.x, self.y = pos
        # self.alex = Turtle(shape='turtle')
        # self.alex.speed(0)
        # self.alex.hideturtle()
        super().__init__(pos)

        self.width = width
        self.height = height
        self.angle = angle

    def draw(self):
        # ajungem la acea pozitie, dar ridicam stiloul prima data
        self.alex.penup()
        self.alex.goto(self.x, self.y)
        # desenam cele 4 linii
        self.alex.pendown()
        self.alex.goto(self.x, self.y + self.height)
        self.alex.goto(self.x + self.width, self.y + self.height)
        self.alex.goto(self.x + self.width, self.y)
        self.alex.goto(self.x, self.y)
        self.alex.penup()

    def movex(self, x):
        self.x = x


class Circle(Drawable):
    def __init__(self, coords: Tuple[int, int], radius: int):
        # self.x, self.y = coords
        # self.alex = Turtle(shape='turtle')
        # self.alex.speed(0)
        # self.alex.hideturtle()
        super().__init__(coords)

        self.radius = radius

    def draw(self):
        # ajungem la acea pozitie, dar ridicam stiloul prima data
        self.alex.penup()
        self.alex.goto(self.x + self.radius, self.y + self.radius)
        # desenam cele 4 linii
        self.alex.pendown()
        self.alex.circle(self.radius)  # TODO dar..
        self.alex.penup()

    def movex(self, x):
        self.x = x

class AnimationEngine:
    # va contine o lista cu obiecte care vor fi animate, o lista cu functiile folosite la update,
    #  dar si FPS
    def __init__(self, elems: List[Drawable], fns: List[Callable], fps: int = 60):
        self.elems = elems
        self.fns = fns
        self.fps = fps

    # si o metoda mainloop() care va executa ceea ce noi scriam in main
    def mainloop(self):
        tracer(0, 0)

        while True:
            # apelezi clear pentru fiecare element
            for d in self.elems:
                d.clear()

            # TODO updatezi pozitia elementelor
            for i in range(len(self.fns)):
                self.fns[i](self.elems[i])

            # redesenezi toate elementele
            for d in self.elems:
                d.draw()

            # urmatoarele 2 randuri nu trebuie modificate
            time.sleep(1 / self.fps)
            update()


def is_inside_square(little: Square, bbox: Rectangle):
    inside_top, inside_right, inside_bottom, inside_left = True, True, True, True
    if little.x + little.side >= bbox.x + bbox.width:  # TODO sper ca side1 este width, dar urmeaza sa verificam
        inside_right = False
    if little.y + little.side >= bbox.y + bbox.height:
        inside_top = False
    # it is outside the left side
    # (cand x este prea mic)
    if little.x <= bbox.x:
        inside_left = False
    if little.y <= bbox.y:
        inside_bottom = False

    # return all inside variables
    return inside_top, inside_right, inside_bottom, inside_left


class CircleSquare(Drawable):
    def __init__(self, coords: Tuple[int, int], radius: int, side: int):
        # self.x, self.y = coords
        # self.alex = Turtle(shape='turtle')
        # self.alex.speed(0)
        # self.alex.hideturtle()
        super().__init__(coords)

        self.radius = radius
        self.side = side

    def draw(self):
        # ajungem la acea pozitie, dar ridicam stiloul prima data
        self.alex.penup()
        self.alex.goto(self.x + self.radius, self.y)
        # desenam cele 4 linii
        self.alex.pendown()
        self.alex.circle(self.radius)  # TODO dar..
        self.alex.penup()
        # putem desena un cerc, chiar din coltul de stanga jos
        self.alex.goto(self.x, self.y)
        self.alex.pendown()
        self.alex.goto(self.x + self.side, self.y)
        self.alex.goto(self.x + self.side, self.y + self.side)
        self.alex.goto(self.x, self.y + self.side)
        self.alex.goto(self.x, self.y)
        self.alex.penup()

    def movex(self, x):
        self.x = x