# master

# using dict for keeping a list of free squares
import math
import random
from itertools import product
from random import randint

maze = [
    [randint(0, 1) for _ in range(5)]
    for _ in range(5)
]

# How to iterate a matrix using a single for:


# {2,3} x {1}    { {2,1}, {3,1} }
# {0,-1} x {2,3}    { 0, 2   0, 3   -1, 2   -1,3 }
for i, j in product(range(3), range(2)):
    print(i, j, end='   ')
print()

# starting from maze, compute a list of position which are free
"""
0 0 1
1 0 0
=>
[[0,0], [0,1], [1,1], [1,2]]
"""
# m = [
#     [0, 0, 1],
#     [1, 0, 0],
# ]
#
# rows = len(m)
# cols = len(m[0])
#
# indexes = [
#     [i, j] # lista
#     for i, j in product(range(rows), range(cols))
#     if m[i][j] == 0
# ]
# print(indexes)

# and after you have the list, create a function which uses the list to choose a random location and return it
"""
e.g. 
Input: [[0,0], [0,1], [1,1], [1,2]]
=>
Output: [0,1]  # it was chosen randomly
"""
free_spaces = [[0, 0], [0, 1], [1, 1], [1, 2]]
i = random.randint(0, 3)  # the random index
drives_position = free_spaces[i]

print(drives_position)

# TODO the code we'll actually use:

# a dictionary which marks the free spaces
"""
e.g. 
Input:  0 0 1
        1 0 0
=>
{0: True, 1: True, 2: True, 3: False, 4: True, 5: False}

 and we can use the dictionary to randomly select an empty position
"""
m = [
    [0, 0, 1],
    [1, 0, 0],
]
rows, cols = len(m), len(m[0])
is_free = {
    (i, j): m[i][j] == 0
    for i, j in product(range(rows), range(cols))
}

print(is_free)

# [1,2]    [1,2,3]
# TODO from a dict we can obtain the indexes
#   we can update the maze
pos = [0, 1]
is_free[tuple(pos)] = False
print(is_free)

# # TODO
# #  we can obtains the list of free position:
# print([
#     [i, j]
#     for i, j in is_free.keys()
#     if is_free[(i, j)]
# ])
# print([
#     list(coord)
#     for coord in is_free.keys()
#     if is_free[coord]
# ])
# TODO
#  or just generate any position, and check whether it's free

while True:
    i = randint(0, rows - 1)
    j = randint(0, cols - 1)
    if is_free[(i, j)]:
        break
print(i, j)

quit()
# Simpler example
l = [0, 3, 10, -2, 19, 3.14]
# create a list with the indexes of the natural numbers
whole = [
    i
    for i in range(len(l))
    if l[i] >= 0 and l[i] == math.floor(l[i])
]
print(whole)
# create a dictionary that stores which numbers are whole
is_whole = {
    i: True if \
        l[i] >= 0 and l[i] == math.floor(l[i]) \
        else False
    for i in range(len(l))
}
print(is_whole)

print(2 if 2 > 3 else 0)

# create a dictionary which contains as keys the indexes of
is_free = {
    (0, 1): True,
    (0, 3): False
}

print(is_free)
print(is_free[(0, 3)])
print(is_free[(0, 1)])
# print(is_free[(0, 2)])  # Error, key not found

# s = set()
# s = {1, 2, 3}
# print(s & {2, 3})
# print(2 in {2, 3})
