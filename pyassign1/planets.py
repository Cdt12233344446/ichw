#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

"""planets.py: A not-to-scale simulation of the Solar System.
               Only first six planets are included.

__author__ = "Cai Danyang"
__pkuid__  = "1700011774"
__email__  = "1700011774@pku.edu.cn"
"""

import math
import turtle

"""set basic parameters
"""
turtle.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.screensize(canvwidth=1500, canvheight=1500, bg="black")
turtle.title("planets.py")
Sun = turtle.Turtle()
Mercury = turtle.Turtle()
Venus = turtle.Turtle()
Earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()
Sun.shape("circle")
Sun.shapesize(0.67, 0.67, 0)
Sun.color("yellow", "yellow")

"""the keys 'bpa' and 'cpa' are created to simplify the expressions in main().
   their values will be evaluated below.
"""
planets_fact = {
    'Mer': {
        'nam': Mercury,
        'dis': 5.79,
        'rad': 7.80,
        'per': 49.0,
        'ecc': 0.45,
        'col': "purple",
        'bpa': 0,
        'cpa': 0,
        },

    'Ven': {
        'nam': Venus,
        'dis': 10.82,
        'rad': 8.71,
        'per': 78.4,
        'ecc': 0.08,
        'col': "orange",
        'bpa': 0,
        'cpa': 0,
        },

    'Ear': {
        'nam': Earth,
        'dis': 14.96,
        'rad': 8.76,
        'per': 100.0,
        'ecc': 0.13,
        'col': "blue",
        'bpa': 0,
        'cpa': 0,
        },

    'Mars': {
        'nam': Mars,
        'dis': 22.79,
        'rad': 8.13,
        'per': 137.1,
        'ecc': 0.31,
        'col': "red",
        'bpa': 0,
        'cpa': 0,
        },

    'Jup': {
        'nam': Jupiter,
        'dis': 77.84,
        'rad': 11.18,
        'per': 344.4,
        'ecc': 0.22,
        'col': "green",
        'bpa': 0,
        'cpa': 0,
        },

    'Sat': {
        'nam': Saturn,
        'dis': 142.67,
        'rad': 11.00,
        'per': 542.6,
        'ecc': 0.23,
        'col': "brown",
        'bpa': 0,
        'cpa': 0,
        },

    }

"""set planets to their initial place
"""
for pls, pls_fct in planets_fact.items():
    pls_fct['nam'].shape("circle")
    pls_fct['nam'].shapesize(pls_fct['rad'] / 20, pls_fct['rad'] / 20, 0)
    pls_fct['nam'].pen(speed=0)
    pls_fct['nam'].color(pls_fct['col'], pls_fct['col'])
    pls_fct['bpa'] = pls_fct['dis'] * math.sqrt(1 - pls_fct['ecc'] ** 2)
    pls_fct['cpa'] = pls_fct['dis'] * pls_fct['ecc']
    pls_fct['nam'].up()
    pls_fct['nam'].goto(pls_fct['dis'] * (1 - pls_fct['ecc']) * 4, 0)
    pls_fct['nam'].down()


def main():
    """main module which motivates the planets
    """
    for t in range(2000):
        for pls, pr in planets_fact.items():
            pr['nam'].goto(
                4 * (pr['dis'] * math.cos(6.283 * t / pr['per']) - pr['cpa']),
                4 * pr['bpa'] * math.sin(6.283 * t / pr['per']))


if __name__ == '__main__':
    main()
