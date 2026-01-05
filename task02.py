"""
Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала 
“дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен 
мати можливість вказати рівень рекурсії.

- Код виконується. Програма візуалізує фрактал “дерево Піфагора”.
-Користувач має можливість вказати рівень рекурсії.
"""

import turtle
import sys
from math import sqrt

def pythagoras_branch(t: turtle.Turtle, degree: int, distance: int):
    """
    Drawing one side of Koch curve
    """
    t.forward(distance)
    if degree > 0:
        t.right(45)
        pythagoras_branch(t, degree-1, distance*sqrt(2)/2)
        t.right(90)
        pythagoras_branch(t, degree-1, distance*sqrt(2)/2)
        t.right(45)
    else:
        t.left(180)
    t.forward(distance)

def pythagoras_tree(t: turtle.Turtle, degree: int, side: int):
    """
    Drawing tree, returning back to same point
    """
    pythagoras_branch(t, degree, side)


def main():
    """
    Entry point
    """
    # Parameter can be passed either as a command line argument, or as a direct input by user.
    # Let's ensure it is an integer with non-negative value
    fractal_iteration = None
    if len(sys.argv)==2:
        try:
            fractal_iteration = int(sys.argv[1])
            if fractal_iteration < 0:
                fractal_iteration = None
        except ValueError:
            pass
    while fractal_iteration is None:
        # let's ask user for input till the correct value is provided
        try:
            fractal_iteration = int(input("Enter Pythagoras tree iterations (number between 0 and 8 is advised): "))
            if fractal_iteration < 1:
                fractal_iteration = None
        except ValueError:
            pass
    try:
        # set screen coordinates and size
        screen = turtle.Screen()
        screen_width = 500
        screen_height = 400
        screen.setup(width=screen_width, height=screen_height)
        screen.setworldcoordinates(0, 0, screen_width, screen_height)
        # initial turtle positioning
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(screen_width/2, 50)
        t.pendown()
        # speedup animation
        t.speed(7)
        t.left(90)

        # draw snowflake
        pythagoras_tree(t, fractal_iteration, 100)
        
        screen.mainloop()
    except turtle.Terminator:
        # ignoring exception when closing the window
        pass


if __name__ == "__main__":
    main()

