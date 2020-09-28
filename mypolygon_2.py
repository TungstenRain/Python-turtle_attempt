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

import turtle
# Instantiate the Turtle
bob = turtle.Turtle()

for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()