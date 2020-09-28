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


def circle(t, r):
    """
        Draws a circle with the given radius.
    
        t: Turtle
        r: radius
    """
    arc(t, r, 360)

# LEVEL 0 PRIMITIVES 
# These are the basic movements defined for the Turtle
# fd, bk, lt, rt, pu, pd

def fd(t, length):
    """
        Move the Turtle forward

        t: Turtle
        length: length to move
    """
    t.fd(length)

def bk(t, length):
    """
        Move the Turtle back

        t: Turtle
        length: length to move
    """
    t.bk(length)

def lt(t, angle=90):
    """
        Turn the Turtle to the left

        t: Turtle
        angle=90: 90 degree angle
    """
    t.lt(angle)

def rt(t, angle=90):
    """
        Turn the Turtle to the right

        t: Turtle
        angle=90: 90 degree angle
    """
    t.rt(angle)

def pd(t):
    """
        Put the pen down

        t: Turtle
    """
    t.pd()

def pu(t):
    """
        Lift the pen up
    
        t: Turtle
    """
    t.pu()

# LEVEL 1 PRIMITIVES 
# These are simple combinations of Level 0 primitives.
# These are basic movements defined for the Turtle
# They have no pre- or post-conditions.

def fdlt(t, n, angle=90):
    """
        Move the Turtle forward and left

        t: Turtle
        n: length to move
        angle=90: 90 degree angle
    """
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    """
        Move the Turtle forward and back

        t: Turtle
        n: length to move
    """
    fd(t, n)
    bk(t, n)

def skip(t, n):
    """
        Lift the pen and move

        t: Turtle
        n: length to move with pen up
    """
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    """
        Makes a vertical line and leave the turtle at the top, facing right

        t: Turtle
        n: length to move the Turtle
        angle=90: 90 degree angle
    """
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    """
        move the turtle vertically and leave it at the top, facing right

        t: Turtle
        n: length to move the Turtle
    """
    lt(t)
    skip(t, n)
    rt(t)

# LEVEL 2 PRIMITIVES use primitives from Levels 0 and 1 to draw posts (vertical elements) and beams (horizontal elements)
# Level 2 primitives ALWAYS return the turtle to the original location and direction.

def post(t, n):
    """
        Makes a vertical line and return to the original position

        t: Turtle
        n: length to move Turtle
    """
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """
        Makes a horizontal line at the given height and return.

        t: Turtle
        n: length to move Turtle
        height: height of the beam
    """
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def hangman(t, n, height):
    """
        Makes a vertical line to the given height and a horizontal line at the given height and then return.
        
        t: Turtle
        n: length to move Turtle
        height: height of the hangman
    """
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

def diagonal(t, x, y):
    """
        Makes a diagonal line to the given x, y offsets and return

        t: Turtle
        x: x-axis coordinate
        y: y-axis coordinate
    """
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    """
        Makes a v shape

        t: Turtle
        n: length to move Turtle
        height: height of v shape
    """
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    """
        Makes a bump with radius n at height*n 

        t: Turtle
        n: radius of the bump
        height: height of the bump
    """
    stump(t, n*height)
    arc(t, n/2.0, 180)
    lt(t)
    fdlt(t, n*height+n)


# Draw the capital letters of the alphabet.

def draw_a(t, n):
    """
        Draw the letter "A"

        t: Turtle
        n: size of the letter
    """
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_b(t, n):
    """
        Draw the letter "B"

        t: Turtle
        n: size of the letter
    """
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    """
        Draw the letter "C"

        t: Turtle
        n: size of the letter
    """
    hangman(t, n, 2)
    fd(t, n)

def draw_d(t, n):
    """
        Draw the letter "D"

        t: Turtle
        n: size of the letter
    """
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    """
        Draws the hangman structure for the letters "E" and "F"

        t: Turtle
        n: size of the letter
    """
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    """
        Draw the letter "E"

        t: Turtle
        n: size of the letter
    """
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    """
        Draw the letter "F"

        t: Turtle
        n: size of the letter
    """
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    """
        Draw the letter "G"

        t: Turtle
        n: size of the letter
    """
    hangman(t, n, 2)
    fd(t, n/2)
    beam(t, n/2, 2)
    fd(t, n/2)
    post(t, n)

def draw_h(t, n):
    """
        Draw the letter "H"

        t: Turtle
        n: size of the letter
    """
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_i(t, n):
    """
        Draw the letter "I"

        t: Turtle
        n: size of the letter
    """
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)

def draw_j(t, n):
    """
        Draw the letter "J"

        t: Turtle
        n: size of the letter
    """
    beam(t, n, 2)
    arc(t, n/2, 90)
    fd(t, 3*n/2)
    skip(t, -2*n)
    rt(t)
    skip(t, n/2)

def draw_k(t, n):
    """
        Draw the letter "K"

        t: Turtle
        n: size of the letter
    """
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    """
        Draw the letter "L"

        t: Turtle
        n: size of the letter
    """
    post(t, 2*n)
    fd(t, n)

def draw_m(t, n):
    """
        Draw the letter "M"

        t: Turtle
        n: size of the letter
    """
    post(t, 2*n)
    draw_v(t, n)
    post(t, 2*n)

def draw_n(t, n):
    """
        Draw the letter "N"

        t: Turtle
        n: size of the letter
    """
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_o(t, n):
    """
        Draw the letter "O"

        t: Turtle
        n: size of the letter
    """
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_p(t, n):
    """
        Draw the letter "P"

        t: Turtle
        n: size of the letter
    """
    bump(t, n, 1)
    skip(t, n/2)

def draw_q(t, n):
    """
        Draw the letter "Q"

        t: Turtle
        n: size of the letter
    """
    draw_o(t, n)
    diagonal(t, -n/2, n)

def draw_r(t, n):
    """
        Draw the letter "R"

        t: Turtle
        n: size of the letter
    """
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    """
        Draw the letter "S"

        t: Turtle
        n: size of the letter
    """
    fd(t, n/2)
    arc(t, n/2, 180)
    arc(t, n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    lt(t)

def draw_t(t, n):
    """
        Draw the letter "T"

        t: Turtle
        n: size of the letter
    """
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    """
        Draw the letter "U"

        t: Turtle
        n: size of the letter
    """
    post(t, 2*n)
    fd(t, n)
    post(t, 2*n)

def draw_v(t, n):
    """
        Draw the letter "V"

        t: Turtle
        n: size of the letter
    """
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    """
        Draw the letter "W"

        t: Turtle
        n: size of the letter
    """
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    """
        Draw the letter "X"

        t: Turtle
        n: size of the letter
    """
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_y(t, n):
    """
        Draw the letter "Y"

        t: Turtle
        n: size of the letter
    """
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n/2)

def draw_z(t, n):
    """
        Draw the letter "Z"

        t: Turtle
        n: size of the letter
    """
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    fd(t, n)

def draw_(t, n):
    """
        Draw a space

        t: Turtle
        n: size of the space
    """
    skip(t, n)

# Instantiate the Turtle
bob = turtle.Turtle()
size = 20

# Hide the Turtle
bob.hideturtle()

for f in [draw_h, draw_e, draw_l, draw_l, draw_o, draw_, draw_t, draw_h, draw_e, draw_r, draw_e]:
    f(bob, size)
    skip(bob, size)

turtle.mainloop()