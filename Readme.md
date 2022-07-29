# Python Turtle and OOP

## Teme

Tema 6 august
1. Inside turtle_3_svg create a new Python Package named mazes.py in care sa creezi o clasa Maze care continee o lista cu rectangles,
   clasa Maze mosteneste Drawable, iar functie draw() are efectul de a dese toate elementele, dar si un boundinb box.
   bbox-ul este primit ca parametrii  pos: Tuple[int, int], width, height
   
maze = Maze((0, 0), 600, 400, ["PUNEM O LISTA CU drawables, care vor fi zidurile maze-ului"])

tip: deoarece implementezi update si clear (clear va da clear*( la toate elementele),
     poti folosi maze-ul intr-un AnimationEngine.

2. Creezi pornind de la propria schita cu cu orice forme (Circle, square, rectangle, poti crea si triunghiuri ca bonus)
   creezi o lista cu niste drawable care sa reprezinte labirintul imaginat de tine.
   






## What should a Python project contains on GitHub

1. Our code :)
2. A .gitignore for Python file
3. A Readme.md describing our code, how to use it, or at least it's functionality
4. Adding a file named `requirements.txt` which describes the packages you installed alongside Python


### Tip

You use 
```shell
pip freeze > requirements.txt
```