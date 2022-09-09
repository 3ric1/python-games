import pygame
import easing_functions

import time

# cand cainele incepe sa mearga, incepe de la viteza 0 (m/s), ajunge pana la viteza 2 (m/s), in 2 secunde
#   1 m/s  este  3.6 km/h


# start_walking = easing_functions.QuadEaseIn(start=0, end=2, duration=2)
#
# print(start_walking(1.2))  # la ce viteza a juns dupa 1.5 secunde
# print(start_walking(1.5))  # la ce viteza a juns dupa 1.5 secunde
# print(start_walking(2))  # la ce viteza a juns dupa 1.5 secunde

pygame.init()
screen_size = screen_width, screen_height = 800, 200

# folosim pygame.SRCALPHA ca in pixelii ecranului sa existe si un canal ALPHA cu transparenta fiecare pixel
screen = pygame.display.set_mode(screen_size, pygame.SRCALPHA)  # e necesar ca sa creeze o fereastra

clock = pygame.time.Clock()
#
# x, y = 50, 50
# speed = 0
# walk_speed = 50
#
# speed_for_time = easing_functions.BounceEaseOut(start=0, end=walk_speed, duration=3)
# init_time = time.time()
#
# while True:
#     dtime = clock.tick(10) / 1000
#     print(dtime)
#
#     # compute the current speed:
#     curr_time = time.time()
#     seconds_since_standing = curr_time - init_time
#     if seconds_since_standing <= 3:
#         speed = speed_for_time(seconds_since_standing)
#     else:
#         speed = 20
#
#     x += speed * dtime
#
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (255, 0, 0), (int(x), 50), 20)
#
#     pygame.display.flip()
#



x, y = 50, 0

height = 0
max_height = 150

height_fn = easing_functions.BounceEaseIn(start=0, end=max_height, duration=5)   # ease in
# height_fn = easing_functions.BounceEaseIn(start=max_height, end=0, duration=5)   # ease Out
# height_fn = easing_functions.BounceEaseIn(start=-2, end=max_height, duration=5)   # ease inBack
init_time = time.time()

while True:
    dtime = clock.tick(10) / 1000
    # print(dtime)

    # compute the current speed:
    curr_time = time.time()
    seconds_since_standing = curr_time - init_time
    if seconds_since_standing <= 5:
        height = height_fn(seconds_since_standing)
    else:
        height = max_height

    x = seconds_since_standing * 25
    y = height

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, 100 - y), 20)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 115, 1000, 100))   # the grass for the ball to bounce on

    pygame.display.flip()

# Ease In Out Back    prastie care loveste o trampulina (sau ceva precum un cearceaf)

# alte 2 exemple practice de animatii