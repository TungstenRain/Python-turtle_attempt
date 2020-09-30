"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 4: Case Study in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""

import turtle


def draw_spiral(t, n, length, init, coil):
    """
        Draws an Archimedian spiral starting at the origin.
    
        n: how many line segments to draw
        length: how long each segment is
        a: how loose the initial spiral starts out (larger is looser)
        coil: how loosly coiled the spiral is (larger is looser)
        http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (init + coil * theta)

        t.lt(dtheta)
        theta += dtheta


# Instantiate the Turtle
bob = turtle.Turtle()
bob.hideturtle()

draw_spiral(bob, n=1000, length=5, init=0.1, coil=0.0005)

turtle.mainloop()