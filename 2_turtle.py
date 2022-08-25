import time
import turtle

from turtle import *
from typing import Tuple, Callable, List


# sam = Turtle(shape='turtle')
#
# sam.color('red', 'yellow')
# sam.begin_fill()
# sam.speed(speed=6)
# while True:
#     sam.forward(200)
#     sam.left(170)
#
#     if abs(sam.pos()) < 1:
#         break
# sam.end_fill()


# Ca sa putem anima ceva, este nevoie sa desenam si sa redesenam obiecte pe ecran.

# asta implica sa stim caracteristicile obiectelor (daca este un patrat, marimea laturii si unghiul de rotatie in planul 2D
# dar avem nevoie si de metoda, de genul draw(), respectiv move()
# Cel mai usor folosim o clasa

# # l = []
# # # tuplu (grup de 1,2,3,4 ... oricate elemente, dar este stiut cate sunt si nu pot fi modificate)
# punct2d = (1, 2)
# punct2d[0] = 3

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


# def main():
#     # sq = Square((0, 0), 3, 0)
#     # sq.move((3, 3))
#
#     # alex = Turtle()
#     # side = 55
#     # # sa desenam un patrat de latura 55 la pozitia 30,100
#     # print(alex.pos())
#     # # ajungem la acea pozitie, dar ridicam stiloul prima data
#     # alex.penup()
#     # alex.goto(30, 100)
#     # # desenam cele 4 linii
#     # x,y = 30, 100
#     # alex.pendown()
#     # alex.goto(x, y+side)
#     # alex.goto(x+side, y+side)
#     # alex.goto(x+side, y)
#     # alex.goto(x, y)
#     # alex.penup()


# TODO tema
#  1. class Circle, care in mod similar creeza metodele move, movex, movey, draw, clear, dar caracterisiticle sunt raza si
#   pozitia de stanga jos a patratului in care este incadrat cercul
#  si sa testezi folosind acelasi while in main (unghiul nu mai are sens sa-l folosesti)
#  2. de creat si un REctangle, cu latime si inaltime diferite.

# if __name__ == '__main__':
#     # patrat = Square((0,0), 33, 0)
#     # patrat.draw()
#     # patrat.move((30, 30))
#     # patrat.draw()
#
#     tracer(0, 0)
#
#     patrat = Square((0,0), 50, 0)
#     x = 0
#     while x < 1000:
#         # apelezi clear pentru fiecare element
#         patrat.clear()
#
#         # updatezi pozitia elementelor
#         x += 3
#         patrat.movex(x)
#
#         # redesenezi elementele
#         patrat.draw()
#
#         # urmatoarele 2 randuri nu trebuie modificate
#         time.sleep(1 / 60)
#         update()
#
#     mainloop()

# Line      ->    doua puncte (Circle) si o linie cu o anumita latime
# Polyline  ->    o lista de linii care trece prin niste puncte


# pygame


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

        A,B,C,D = (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), \
                  (self.x + self.width, self.y), (self.x, self.y)

        A_rotated = rotate((self.x, self.y), A, self.angle)
        B_rotated = rotate((self.x, self.y), B, self.angle)
        C_rotated = rotate((self.x, self.y), C, self.angle)
        D_rotated = rotate((self.x, self.y), D, self.angle)

        self.alex.goto(*A_rotated)
        self.alex.goto(*B_rotated)
        self.alex.goto(*C_rotated)
        self.alex.goto(*D_rotated)
        self.alex.penup()

    def movex(self, x):
        self.x = x


# if __name__ == '__main__':
#     # patrat = Square((0,0), 33, 0)
#     # patrat.draw()
#     # patrat.move((30, 30))
#     # patrat.draw()
#
#     tracer(0, 0)
#
#     dreptunghi = Rectangle((0,0), 150, 90, 0)
#     x = 0
#     while x < 1000:
#         # apelezi clear pentru fiecare element
#         dreptunghi.clear()
#
#         # updatezi pozitia elementelor
#         x += 3
#         dreptunghi.movex(x)
#
#         # redesenezi elementele
#         dreptunghi.draw()
#
#         # urmatoarele 2 randuri nu trebuie modificate
#         time.sleep(1 / 60)
#         update()
#
#     mainloop()


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


# if __name__ == '__main__':
#     # patrat = Square((0,0), 33, 0)
#     # patrat.draw()
#     # patrat.move((30, 30))
#     # patrat.draw()
#
#     tracer(0, 0)
#
#     cerc = Circle((0,0), 50)
#     x = 0
#     while x < 1000:
#         # apelezi clear pentru fiecare element
#         cerc.clear()
#
#         # updatezi pozitia elementelor
#         x += 3
#         cerc.movex(x)
#
#         # redesenezi elementele
#         cerc.draw()
#
#         # urmatoarele 2 randuri nu trebuie modificate
#         time.sleep(1 / 60)
#         update()
#
#     mainloop()


# TODO haide sa cream 5 cercuri care se invart in jurul unui patrat.

# sa spunem ca vom avea   -100, -100     100, -100,    100, 100     -100, 100
# iar cercurile au initial raza 50


# if __name__ == '__main__':
#     tracer(0, 0)
#
#     patrat = Square((-50, 0), 200, 0)
#     lista = [
#         Circle((-100, -100), 50),
#         Circle((100, -100), 50),
#         Circle((100, 100), 50),
#         Circle((-100, 100), 50)
#     ]
#     FPS = 60
#
#     while True:
#         # apelezi clear pentru fiecare element
#         patrat.clear()
#         for cerc in lista:
#             cerc.clear()
#
#         # updatezi pozitia elementelor
#         # Daca un cerc se afla pe linia de sus, adica y-ul lui este 100
#         #  scade x-ul, ca sa se deplaseze spre stanga
#         # Daca un cerc se afla pe coloana din stanga  daca x este -100
#         #  scade y-ul
#         for cerc in lista:
#             if cerc.y == 100 and cerc.x > - 100:
#                 cerc.x -= 1
#             elif cerc.x == - 100 and cerc.y > - 100:
#                 cerc.y -= 1
#             elif cerc.y == - 100 and cerc.x < 100:
#                 cerc.x += 1
#             elif cerc.x == 100 and cerc.y < 100:
#                 cerc.y += 1
#         # logica care determina cercurile sa se invarta
#
#         # redesenezi toate elementele
#         patrat.draw()
#         for cerc in lista:
#             cerc.draw()
#
#         # urmatoarele 2 randuri nu trebuie modificate
#         time.sleep(1 / FPS)
#         update()
#
#     mainloop()

# TODO info: in Python functiile sunt tot variable, deci pot fi reatribuite si folosite ca argumente in functii
# def afis(val: int):
#     print(val)
#

# afis(10)
#
# var = afis
# var(11)
# quit()


# TODO folosirea functiilor ca argumente pentru a implement o functie care ruleaza pentru noi animatia, dar ii putem spune printr-un callback cum sa se miste elementul cerc

# def animation_loop(circle: Circle, anim_fn: Callable):  # Callableinseamna variabila care retine o functie
#     tracer(0, 0)
#
#     FPS = 60
#
#     while True:
#         # apelezi clear pentru fiecare element
#         circle.clear()
#
#         # updatezi pozitia elementelor
#         anim_fn(circle)
#
#         # redesenezi toate elementele
#         circle.draw()
#
#         # urmatoarele 2 randuri nu trebuie modificate
#         time.sleep(1 / FPS)
#         update()
#
#     mainloop()
#
#
# if __name__ == '__main__':
#     circle = Circle((0, 0), 10)
#
#
#     def update_fn(circle: Circle):
#         circle.x += 1
#         print(circle.x)
#
#
#     def update_fn2(circle: Circle):
#         circle.x += 3
#         circle.y += 1
#         print(circle.x)
#
#
#     animation_loop(circle, update_fn2)

# TODO inheritance/ mostenirea in POO

# class Moveable:
#     def __init__(self, coords: Tuple[int, int]):
#         self.x, self.y = coords
#
#     def move(self, coords: Tuple[int, int]):
#         self.x, self.y = coords
#
#     def __str__(self):
#         return f'Movaable(x: {self.x}, y: {self.y})'
#
#
# class MoveableCircle(Moveable):
#     def __init__(self, coords: Tuple[int, int], radius: int):
#         super().__init__(coords)
#         # Moveable.__init__(self, coords)
#         self.radius = radius
#
#     def __str__(self):
#         return f'MovaableCircle(x: {self.x}, y: {self.y}, radius: {self.radius})'
#
#
# # clasele pot fi foloti precum niste interfete, adica putem avea o classa aproape goala, care contine doar metode specifice mai multe
# # tipuri de obiecte (e.g. Square, Rectangle, Circle   contin metodele clear(), draw()
#
#
# # if __name__ == '__main__':
# #     m = Moveable((2, 3))
# #     m.move((3, 3))
# #     c = MoveableCircle((3, 17), 10)
#     c.move((3, 3))
#     print(m, c)


# # Putem crea o lista cu obiecte de tipul Drawable
# if __name__ == '__main__':
#     # l: List[Drawable] = []  # List[Drawble] l = {};
#     # l.append(
#     #     Circle((0, 0), 100)
#     # )
#     # l.append(
#     #     Square((0, 0), 70, 0)
#     # )
#     # functiile de update ale obiectelor animate:
#     def update_circle(circle: Circle):
#         circle.x += 1
#         circle.y += 1
#     def update_square(circle: Circle):
#         circle.x += 1.5
#         circle.y += 1.5
#
#
#     fns = [
#         update_circle,
#         update_square
#     ]
#     elems = [
#         Circle((0, 0), 100),
#         Square((0, 0), 70, 0)
#     ]
#
#
#
#     tracer(0, 0)
#     FPS = 60
#
#     while True:
#         # apelezi clear pentru fiecare element
#         for d in elems:
#             d.clear()
#
#         # TODO updatezi pozitia elementelor
#         for i in range(len(fns)):
#             fns[i](elems[i])
#
#         # redesenezi toate elementele
#         for d in elems:
#             d.draw()
#
#         # urmatoarele 2 randuri nu trebuie modificate
#         time.sleep(1 / FPS)
#         update()
#
#     mainloop()


# class AnimationEngine:
#     # va contine o lista cu obiecte care vor fi animate, o lista cu functiile folosite la update,
#     #  dar si FPS
#     def __init__(self, elems: List[Drawable], fns: List[Callable], fps: int = 60):
#         self.elems = elems
#         self.fns = fns
#         self.fps = fps
#
#     # si o metoda mainloop() care va executa ceea ce noi scriam in main
#     def mainloop(self):
#         tracer(0, 0)
#
#         while True:
#             # apelezi clear pentru fiecare element
#             for d in self.elems:
#                 d.clear()
#
#             # TODO updatezi pozitia elementelor
#             for i in range(len(self.fns)):
#                 self.fns[i](self.elems[i])
#
#             # redesenezi toate elementele
#             for d in self.elems:
#                 d.draw()
#
#             # urmatoarele 2 randuri nu trebuie modificate
#             time.sleep(1 / self.fps)
#             update()
#
#
# # Exemlu utilizare AnimationEngine
# if __name__ == '__main__':
#     def update_circle(circle: Circle):
#         circle.x += 1
#         circle.y += 1
#     def update_square(square: Square):
#         square.x += 1.5
#         square.y += 1.5
#     def update_square2(square: Square):
#         square.side += 2
#
#
#     fns = [
#         update_circle,
#         update_square2
#     ]
#     elems = [
#         Circle((0, 0), 100),
#         Square((0, 0), 100, 0)
#     ]
#     engine = AnimationEngine(
#         elems,
#         fns,
#         fps=60
#     )
#     engine.mainloop()


# Creeaza un cerc si un patrat, patratul de latura 100 si cercul de raza 50
# , cu cercul incadrat in patrat in mod perfect, si se deplaseaza in acelasi ritm (alegi tu ritmul, adica cu cat creste x si y)
#  intr-

# hint pt jocul cu animarea cu delay, precum la engine,
#  ai putea folosi un delay cu ajutorul unor variabile globale de tipul:
rect1_delay = 200


# si la fie frame, tu stii ca au trecut 1000/fps milisecunde

# Dupa aceea vom crea un mini engine, care animeaza pentru noi cercurile

import math

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in hexadecimal degrees.
    """
    ox, oy = origin
    px, py = point

    angle = math.radians(angle)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

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


# #Cerc inscris intr-un patrat
# if __name__ == '__main__':
#     def update_circle(circle: Circle):
#         circle.x += 1.5
#         circle.y += 1.5
#     def update_square(square: Square):
#         square.x += 1.5
#         square.y += 1.5
#
#     def do_nothing(elem: Drawable):
#         pass
#
#
#     fns = [
#         update_circle,
#         update_square
#     ]
#     elems = [
#         Circle((0, -50), 50),
#         Square((0, 0), 100, 0),
#     ]
#     engine = AnimationEngine(
#         elems,
#         fns,
#         fps=60
#     )
#     engine.mainloop()

# ma mai auzi, ERic?
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


# if __name__ == '__main__':
#     dx = 1.5
#     dy = 1.5
#     bx = 1
#     by = 1
#
#
#     def update_circle(circle: Circle):
#         global dx, dy
#         circle.x += dx
#         circle.y += dy
#
#
#     def update_bbox(bbox: Rectangle):
#         global bx, by
#         bbox.x += bx
#         bbox.y += bx
#
#
#     def update_square(square: Square):
#         global dx, dy
#         square.x += dx
#         square.y += dy
#         # sa detectam coliziunea, adica faptul ca cercul s-a intersectat cu bbox-ul
#         top, right, bottom, left = is_inside_square(square, bbox_rectangle)
#         # daca oricare dintre inside-uri este False:
#         # cand detectam, schimbam directia de deplasare, adica dx-ul si dy-ul
#
#         # retinem in contorul
#         if top == False:
#             dy = -1.5
#         if right == False:
#             dx = -1.5
#         if bottom == False:
#             dy = 1.5
#         if left == False:
#             dx = 1.5
#
#
#     def do_nothing(elem: Drawable):
#         pass
#
#
#     bounding_box_width = 300 + 70
#     bounding_box_height = 100 + 70
#     bbox_rectangle = Rectangle((-bounding_box_width // 2, -bounding_box_height // 2), bounding_box_width,
#                                bounding_box_height, 0)
#     side_box = 70
#
#     fns = [
#         update_circle,
#         update_square,
#         update_bbox
#     ]
#     elems = [
#         Circle((-side_box // 2, -side_box), side_box // 2),
#         Square((-side_box // 2, -side_box // 2), side_box, 0),
#         bbox_rectangle  # the bounding box
#     ]
#     engine = AnimationEngine(
#         elems,
#         fns,
#         fps=60
#     )
#     engine.mainloop()




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


# # test whether the circle square works
# if __name__ == '__main__':
#
#     def update_circlesquare(circlesquare:Drawable):
#         circlesquare.x += 1.5
#         circlesquare.y += 1.5
#
#     fns = [
#         update_circlesquare
#     ]
#     elems = [
#         CircleSquare((0,0), 10, 20),
#     ]
#     engine = AnimationEngine(
#         elems,
#         fns,
#         fps=60
#     )
#     engine.mainloop()

# if __name__ == '__main__':
#     cs_speed = 50
#     dx = cs_speed
#     dy = cs_speed
#     bx = 1
#     by = 1
#
#
#     def update_circle(circle: Circle):
#         global dx, dy
#         circle.x += dx
#         circle.y += dy
#
#
#     def update_bbox(bbox: Rectangle):
#         global bx, by
#         bbox.x += bx
#         bbox.y += bx
#
#
#     def update_circle_square(circlesquare: CircleSquare):
#         global dx, dy
#         circlesquare.x += dx
#         circlesquare.y += dy
#         # sa detectam coliziunea, adica faptul ca cercul s-a intersectat cu bbox-ul
#         top, right, bottom, left = is_inside_square(circlesquare, bbox_rectangle)
#         # daca oricare dintre inside-uri este False:
#         # cand detectam, schimbam directia de deplasare, adica dx-ul si dy-ul
#
#         # retinem in contorul
#         if top == False:
#             dy = -cs_speed
#         if right == False:
#             dx = -cs_speed
#         if bottom == False:
#             dy = cs_speed
#         if left == False:
#             dx = cs_speed
#
#
#     def do_nothing(elem: Drawable):
#         pass
#
#
#     bounding_box_width = 300 + 70
#     bounding_box_height = 100 + 70
#     bbox_rectangle = Rectangle((-bounding_box_width // 2, -bounding_box_height // 2), bounding_box_width,
#                                bounding_box_height, 0)
#     side_box = 70
#
#     fns = [
#         update_circle_square,
#         update_bbox
#     ]
#     elems = [
#         CircleSquare((-side_box // 2, -side_box // 2), side_box, 2 * side_box),
#         bbox_rectangle  # the bounding box
#     ]
#     engine = AnimationEngine(
#         elems,
#         fns,
#         fps=60
#     )
#     engine.mainloop()

class Maze(Drawable):
    def __init__(self, pos: Tuple[int, int], elems: List[Drawable]):
        super().__init__(pos)
        self.elems = elems

    def draw(self):
        for elem in self.elems:
            elem.draw()

    def clear(self):
        for elem in self.elems:
            elem.clear()

    def update(self):
        # show the updated canvas
        update()  # update the screen

    def set_angle(self, angle):
        for elem in self.elems:
            elem.angle = angle


if __name__ == '__main__':
    maze = Maze((0, 0), [
        Rectangle((0, 0), 100, 10, 0),
        Rectangle((0, 0), 10, 100, 0),
        Rectangle((90, 0), 10, 100, 0),
        Rectangle((0, 90), 100, 10, 0),
    ])

    tracer(0, 0)  # elimin

    angle = 0
    while angle < 1000:
        # apelezi clear pentru fiecare element
        maze.clear()

        # # updatezi pozitia elementelor
        angle += 1
        maze.set_angle(angle)

        # redesenezi elementele
        maze.draw()

        # urmatoarele 2 randuri nu trebuie modificate
        time.sleep(1 / 5)
        maze.update()

    mainloop()