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

def arc(t, r, angle):
    """
        Draws an arc with the given radius and angle.
        t: Turtle
        r: radius
        angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    """
        Draws a petal using two arcs

        t: Turtle
        r: radius of the arcs
        angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    """
        Draws a flower with n petals

        t: Turtle
        n: number of petals
        r: radius of the arcs
        angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move(t, length):
    """
        Move the Turtle (t) forward by length units without leaving a trail

        t: Turtle
        length: unit moved
    """
    t.pu()
    t.fd(length)
    t.pd()

# Instantiate the Turtle
bob = turtle.Turtle()

# Hide bob and it still draws
bob.hideturtle()

# Draw a sequence of 3 flowers
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

turtle.mainloop()