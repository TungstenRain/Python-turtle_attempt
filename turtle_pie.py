"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    Copyright 2015 Allen B. Downey
    License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

    This is to test out the turtle module from Chapter 4: Case Study in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""

import math
import turtle

def draw_pie(t, n, r):
    """
        Draws a pie, then moves into position to the right.
    
        t: Turtle
        n: number of segments
        r: length of the radial spokes
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

def polypie(t, n, r):
    """
        Draws a pie divided into radial segments.
    
        t: Turtle
        n: number of segments
        r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)


def isosceles(t, r, angle):
    """
        Draws an icosceles triangle.
        The turtle starts and ends at the peak, facing the middle of the base.
    
        t: Turtle
        r: length of the equal legs
        angle: half peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


bob = turtle.Turtle()
bob.hideturtle()

bob.pu()
bob.bk(130)
bob.pd()

# draw polypies with various number of sides
size = 50
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)

turtle.mainloop()