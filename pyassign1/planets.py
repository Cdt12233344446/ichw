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

"""the keys 'b' and 'c' are geometric factors
   created to simplify the expressions in main() and will be evaluated below
"""
planets_and_parameters = [
    {'i': Mercury,
     'rad': 1.53,
     'per': 24.1,
     'col': "purple",
     'a': 5.79,
     'e': 0.206,
     'b': 0,
     'c': 0,
     },

    {'i': Venus,
     'rad': 3.80,
     'per': 61.5,
     'col': "orange",
     'a': 10.82,
     'e': 0.007,
     'b': 0,
     'c': 0,
     },

    {'i': Earth,
     'rad': 4.00,
     'per': 100.0,
     'col': "blue",
     'a': 14.96,
     'e': 0.016,
     'b': 0,
     'c': 0,
     },

    {'i': Mars,
     'rad': 2.13,
     'per': 188.0,
     'col': "red",
     'a': 22.79,
     'e': 0.093,
     'b': 0,
     'c': 0,
     },

    {'i': Jupiter,
     'rad': 11.2,
     'per': 1186,
     'col': "green",
     'a': 77.84,
     'e': 0.048,
     'b': 0,
     'c': 0,
     },

    {'i': Saturn,
     'rad': 9.45,
     'per': 2945,
     'col': "brown",
     'a': 142.67,
     'e': 0.054,
     'b': 0,
     'c': 0,
     },

    ]

# sends planets to their initial position
for pls in planets_and_parameters:
    pls['i'].shape("circle")
    pls['i'].shapesize(pls['rad'] / 20, pls['rad'] / 20, 0)
    pls['i'].color(pls['col'], pls['col'])
    pls['b'] = pls['a'] * m.sqrt(1 - pls['e'] ** 2)
    pls['c'] = pls['a'] * pls['e']
    pls['i'].up()
    pls['i'].goto(pls['a'] * (1 - pls['e']) * 4, 0)
    pls['i'].down()


def main():
    """keeps the planets going
    """
    try:
        for t in range(1, 200):
            for pl in planets_and_parameters:
                pl['i'].goto(
                    4 * (pl['a'] * m.cos(2 * m.pi * t / pl['per']) - pl['c']),
                    4 * pl['b'] * m.sin(2 * m.pi * t / pl['per']))

        # avoids redundant rendering by 'upping' the faster planets
        if t == 100:
            for pls in planets_and_parameters[:3]:
                pls['i'].up()
    except:
        pass
    finally:
        print("Thanks for watching this simulaton. See you next time!")

if __name__ == '__main__':
    main()
