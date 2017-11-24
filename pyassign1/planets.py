#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

"""planets.py: An almost-to-scale simulation of the Solar System.
               Only first six planets are included.

__author__ = "Cai Danyang"
__pkuid__  = "1700011774"
__email__  = "1700011774@pku.edu.cn"
"""

import math as m
import turtle
import random as ran

# defines objects
turtle.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.screensize(canvwidth=1500, canvheight=1500, bg="black")
turtle.bgpic("Orrery.gif")
turtle.title("planets.py")
Sun = turtle.Turtle()
Mercury = turtle.Turtle()
Venus = turtle.Turtle()
Earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()
Sun.shape("circle")
Sun.shapesize(1.09, 1.09, 0)
Sun.color("yellow", "yellow")

"""
A list of parameters needed for the following codes. Here
'i' is the index or 'self' parameter,
'rad' determines the size of the planet,
'col' is the designated color,
'φ' is the 'phase' that will be randomized later,
'a' is the semimajor axis,
'e' defines the eccentricity of the orbit,
'b' and 'c' are auxillary and will be assigned values immediately after.
"""
planets_and_parameters = [
    {'i': Mercury,
     'rad': 1.53,
     'per': 24.1,
     'col': "purple",
     'φ': 0,
     'a': 5.79,
     'e': 0.206,
     'b': 0,
     'c': 0,
     },

    {'i': Venus,
     'rad': 3.80,
     'per': 61.5,
     'col': "orange",
     'φ': 0,
     'a': 10.82,
     'e': 0.007,
     'b': 0,
     'c': 0,
     },

    {'i': Earth,
     'rad': 4.00,
     'per': 100.0,
     'col': "blue",
     'φ': 0,
     'a': 14.96,
     'e': 0.016,
     'b': 0,
     'c': 0,
     },

    {'i': Mars,
     'rad': 2.13,
     'per': 188.0,
     'col': "red",
     'φ': 0,
     'a': 22.79,
     'e': 0.093,
     'b': 0,
     'c': 0,
     },

    {'i': Jupiter,
     'rad': 11.2,
     'per': 1186,
     'col': "green",
     'φ': 0,
     'a': 77.84,
     'e': 0.048,
     'b': 0,
     'c': 0,
     },

    {'i': Saturn,
     'rad': 9.45,
     'per': 2945,
     'col': "brown",
     'φ': 0,
     'a': 142.67,
     'e': 0.054,
     'b': 0,
     'c': 0,
     },

    ]


def init():
    """sends planets to their initial position
    """
    for pls in planets_and_parameters:
        pls['i'].shape("circle")
        pls['i'].shapesize(pls['rad'] / 20, pls['rad'] / 20, 0)
        pls['i'].color(pls['col'], pls['col'])
        pls['i'].speed(0)
        pls['φ'] = ran.uniform(-m.pi, m.pi)
        pls['b'] = pls['a'] * m.sqrt(1 - pls['e'] ** 2)
        pls['c'] = pls['a'] * pls['e']
        pls['i'].up()
        pls['i'].goto(
            4 * (pls['a'] * m.cos(pls['φ']) - pls['c']),
            4 * pls['b'] * m.sin(pls['φ']))
        pls['i'].down()


def main():
    """keeps the planets going
    """
    try:
        for t in range(1, 2000):
            for pl in planets_and_parameters:
                # use φ to simplify the expression, again
                pl['φ'] = pl['φ'] + 2 * m.pi / pl['per']
                pl['i'].goto(
                    4 * (pl['a'] * m.cos(pl['φ']) - pl['c']),
                    4 * pl['b'] * m.sin(pl['φ']))

                # avoids redundant rendering by 'upping' the faster planets
                if t == 100:
                    for pls in planets_and_parameters[:3]:
                        pls['i'].up()
    except:
        print("Pity that you quit so early. See you next time!")
    else:
        print("Thanks for watching this simulaton. See you next time!")


if __name__ == '__main__':
    init()
    main()
