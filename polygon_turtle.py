"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    Chapter 4: Case Study in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""

import math
import turtle

def square(t, length):
    """
        Draws a square with sides of the given length.

        Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):
    """
        Draws n line segments.
        
        t: Turtle object
        n: number of line segments
        length: length of each segment
        angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """
        Draws a polygon with n sides.
        
        t: Turtle
        n: number of sides
        length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """
        Draws an arc with the given radius and angle.
        
        t: Turtle
        r: radius
        angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    # making a slight left turn before starting reduces the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    """
        Draws a circle with the given radius.
        
        t: Turtle
        r: radius
    """
    arc(t, r, 360)

# Instantiate the Turtle
bob = turtle.Turtle()

"""
square(bob, 40)
polygon(bob, 200, 5)
polygon(bob, 100, 6)
polygon(bob, 50, 8)
polygon(bob, 25, 10)
circle(bob, 50)
circle(bob, 25)
"""
arc(bob, 40, 90)

turtle.mainloop()